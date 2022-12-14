from setuptools import find_packages, setup

setup(
    name='mlops_homework',
    packages=find_packages(),
    version='0.1.0',
    description='Homework MADE 2022 MLOps',
    author='tupiznak',
    license='',
    entry_points={
        "console_scripts": [
            "mlops_homework_download_dataset = mlops_homework.data.load_dataset:main",
            "mlops_homework_make_eda = mlops_homework.data.make_eda:main",
            "mlops_homework_process_dataset = mlops_homework.features.build_features:main",
            "mlops_homework_train_model = mlops_homework.models.train_model:main",
            "mlops_homework_predict_baseline_model = mlops_homework.models.baseline.predict_baseline_model:main",
        ]
    },
)
