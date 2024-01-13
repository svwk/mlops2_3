import datetime as dt
import os
from datetime import timedelta

from airflow.operators.bash import BashOperator
from airflow import DAG

project_path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
# # %% Задание путей для файлов
data_file_path = os.path.join(project_path, "data", "raw_data.csv")
script_dir_path = os.path.join(project_path, "scripts")

args = {
    "owner": "admin",
    "start_date": dt.datetime(2024, 1, 1),
    'provide_context': True,
    'schedule_interval': timedelta(minutes=10),
}
 
with DAG(
    dag_id='youtube_likes_score',
    default_args=args,
    schedule_interval=None,
    tags=['youtube', 'score'],
) as dag:
    get_data = BashOperator(task_id='get_data',
                            bash_command=f"python3 {os.path.join(script_dir_path, 'get_data.py')} '{project_path}'",
                            dag=dag)
    process_data = BashOperator(task_id='process_data',
                            bash_command=f"python3 {os.path.join(script_dir_path, 'process_data.py')} '{project_path}'",
                            dag=dag)
    train_test_split_data = BashOperator(task_id='train_test_split_data',
                            bash_command=f"python3 {os.path.join(script_dir_path, 'train_test_split.py')} '{project_path}'",
                            dag=dag)  
    train_model = BashOperator(task_id='train_model',
                            bash_command=f"python3 {os.path.join(script_dir_path, 'train_model.py')} '{project_path}'",
                            dag=dag)
    test_model = BashOperator(task_id='test_model',
                            bash_command=f"python3 {os.path.join(script_dir_path, 'test_model.py')} '{project_path}'",
                            dag=dag)

    get_data >> process_data >> train_test_split_data >> train_model >> test_model