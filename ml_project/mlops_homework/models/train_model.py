import os

import dvc.api
import hydra
from dotenv import load_dotenv, find_dotenv
from mlflow import set_tracking_uri, log_param

from mlops_homework.conf.config import Config, PROJECT_PATH
from .baseline.train_baseline_model import train_model

os.environ["AWS_ACCESS_KEY_ID"] = "11111111"
os.environ["AWS_SECRET_ACCESS_KEY"] = "22222222"
os.environ["MLFLOW_S3_ENDPOINT_URL"] = f"http://localhost:9000/"
os.environ["MLFLOW_TRACKING_URI"] = f"http://localhost:5000/"


@hydra.main(version_base=None, config_path='../conf', config_name="config")
def main(cfg: Config):
    load_dotenv(find_dotenv())
    set_tracking_uri(os.environ['MLFLOW_TRACKING_URI'])
    dvc_params = dvc.api.params_show()
    [setattr(cfg, k, v) for k, v in dvc_params.items()]
    log_param('test_split_size', cfg.model.test_split.size)
    log_param('random_state', cfg.random_state)
    log_param('encode_strategy', cfg.preprocessing.categorical_features)
    if cfg.model.name == 'baseline':
        train_model(config_model=cfg.model,
                    data_path=PROJECT_PATH + cfg.relative_path_to_data_processed_csv,
                    model_path=PROJECT_PATH + cfg.relative_path_to_model)
    else:
        raise NotImplementedError('incorrect model')
