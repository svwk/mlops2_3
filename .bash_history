mc
python3 -v
python3 -m venv airflow_venv
source airflow_venv/bin/activate
dractivate
deactivate
sudo apt-get update -y && sudo apt-get install software-properties-common -y && sudo apt-get install python-setuptools -y && sudo apt install libpq-dev -y && sudo apt install postgresql -y && sudo pip install psycopg2
source airflow_venv/bin/activate
pip install psycopg2
export AIRFLOW_HOME=~/airflow
pip3 install apache-airflow
airflow -v
airflow version
pip install mlflow
pip freeze
export AIRFLOW_HOME=~/airflow
deactivate
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
sudo apt install pgadmin4
sudo apt install pgadmin4-web
sudo -u postgres psql
export AIRFLOW_HOME=~/airflow
sudo -u postgres psql
airflow db init
source airflow_venv/bin/activate
airflow db init
source airflow_venv/bin/activate
airflow scheduler
pip install -r requirements.txt
airflow scheduler
