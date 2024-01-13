from pyyoutube import Api
import os
import sys
import mlflow
from mlflow.tracking import MlflowClient

project_path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
if len(sys.argv) == 2:
    project_path = sys.argv[1]

# # %% Задание путей для файлов
data_file_path = os.path.join(project_path, "data", "raw_data.csv")
script_file_path = os.path.join(project_path, "scripts", "get_data.py")
mlflow_dir = os.path.join(project_path, "mlflow")

os.environ["MLFLOW_REGISTRY_URI"] = mlflow_dir
mlflow.set_tracking_uri("http://prod_srv:5010")
mlflow.set_experiment("get_data")

key = "AIzaSyC1AAlA9qySoBr7daw_CoSyPb3nYLuoWPI"
api = Api(api_key=key)
video_id='2FbrQ189wis'
video = api.get_video_by_id(video_id=video_id)
s=video.items[0].statistics.likeCount

with open(data_file_path, 'a') as f:
    f.write("{}\n".format(s))

with mlflow.start_run():
    mlflow.log_artifact(local_path=script_file_path, artifact_path="get_data")
    mlflow.log_param("likes_count", s)
    mlflow.log_artifact(local_path=data_file_path, artifact_path="get_data")
    mlflow.end_run()
