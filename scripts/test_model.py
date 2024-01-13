from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
import os
import sys

import mlflow
from mlflow.tracking import MlflowClient


# # %% Задание путей для файлов
project_path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
if len(sys.argv) == 2:
    project_path = sys.argv[1]

test_data_file_path = os.path.join(project_path, "data", "test_data.csv")
model_file_path = os.path.join(project_path, "models", "data.pickle")
script_file_path = os.path.join(project_path, "scripts", "test_model.py")
mlflow_dir = os.path.join(project_path, "mlflow")

# Настройки MLFlow
os.environ["MLFLOW_REGISTRY_URI"] = mlflow_dir
mlflow.set_tracking_uri("http://prod_srv:5010")
mlflow.set_experiment("test_model")

df = pd.read_csv(test_data_file_path, header=None)
df.columns = ['id', 'counts']
 
model = LinearRegression()
with open(model_file_path, 'rb') as f:
    model = pickle.load(f)
 
score = model.score(df['id'].values.reshape(-1,1), df['counts'])
print("score=", score)

# Логирование в MLFlow
with mlflow.start_run():
    mlflow.log_metric("score", score)
    mlflow.end_run()