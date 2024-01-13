import sys
import pandas as pd
import os

import mlflow
from mlflow.tracking import MlflowClient

project_path = os.path.abspath(os.path.join(os.getcwd(),  os.path.pardir))
if len(sys.argv) == 2:
    project_path = sys.argv[1]

# # %% Задание путей для файлов
raw_data_file_path = os.path.join(project_path, "data", "raw_data.csv")
processed_data_file_path = os.path.join(project_path, "data", "processed_data.csv")
script_file_path = os.path.join(project_path, "scripts", "process_data.py")
mlflow_dir = os.path.join(project_path, "mlflow")

os.environ["MLFLOW_REGISTRY_URI"] = mlflow_dir
mlflow.set_tracking_uri("http://prod_srv:5010")
mlflow.set_experiment("process_data")

df = pd.read_csv(raw_data_file_path, header=None)

# вычитаем минимальное значение с каждого элемента делим на разницу максимального и минимального
df[0] = (df[0] - df[0].min()) / (df[0].max() - df[0].min())

with open(processed_data_file_path, 'w') as f:
    for i, item in enumerate(df[0].values):
        f.write("{},{}\n".format(i, item))

with mlflow.start_run():
    mlflow.log_artifact(local_path=script_file_path, artifact_path="process_data")
    mlflow.log_artifact(local_path=processed_data_file_path, artifact_path="process_data")
    mlflow.end_run()