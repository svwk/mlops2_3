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

train_data_file_path = os.path.join(project_path, "data", "train_data.csv")
model_file_path = os.path.join(project_path, "models", "data.pickle")
script_file_path = os.path.join(project_path, "scripts", "train_model.py")
mlflow_dir = os.path.join(project_path, "mlflow")

# Настройки MLFlow
os.environ["MLFLOW_REGISTRY_URI"] = mlflow_dir
mlflow.set_tracking_uri("http://prod_srv:5010")
mlflow.set_experiment("train_model")
 
df = pd.read_csv(train_data_file_path, header=None)
df.columns = ['id', 'counts']
model = LinearRegression()

# Логирование в MLFlow
with mlflow.start_run():
    mlflow.sklearn.log_model(model,
                             artifact_path="train_model",
                             registered_model_name="log_reg_model")
    mlflow.log_artifact(local_path=script_file_path, artifact_path="train_model")
    mlflow.end_run()
 
model.fit(df['id'].values.reshape(-1,1), df['counts'])

# Сохранение результатов в файл
with open(model_file_path, 'wb') as f:
    pickle.dump(model, f)