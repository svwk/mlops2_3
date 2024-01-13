import pandas as pd
import numpy as np
import os
import sys
import mlflow
from mlflow.tracking import MlflowClient


# # %% Задание путей для файлов
project_path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
if len(sys.argv) == 2:
    project_path = sys.argv[1]

processed_data_file_path = os.path.join(project_path, "data", "processed_data.csv")
train_data_file_path = os.path.join(project_path, "data", "train_data.csv")
test_data_file_path = os.path.join(project_path, "data", "test_data.csv")
script_file_path = os.path.join(project_path, "scripts", "train_test_split.py")
mlflow_dir = os.path.join(project_path, "mlflow")

# Настройки MLFlow
os.environ["MLFLOW_REGISTRY_URI"] = mlflow_dir
mlflow.set_tracking_uri("http://prod_srv:5010")
mlflow.set_experiment("train_test_split")

df = pd.read_csv(processed_data_file_path, header=None)

idxs = np.array(df.index.values)
np.random.shuffle(idxs)
l = int(len(df) * 0.7)
train_idxs = idxs[:l]
test_idxs = idxs[l + 1:]

# Сохранение результатов в файл
df.loc[train_idxs, :].to_csv(train_data_file_path, header=None, index=None)
df.loc[test_idxs, :].to_csv(test_data_file_path, header=None, index=None)

# Логирование в MLFlow
with mlflow.start_run():
    mlflow.log_artifact(local_path=script_file_path, artifact_path="train_test_split")
    mlflow.log_artifact(local_path=train_data_file_path, artifact_path="train_test_split")
    mlflow.log_artifact(local_path=test_data_file_path, artifact_path="train_test_split")
    mlflow.end_run()