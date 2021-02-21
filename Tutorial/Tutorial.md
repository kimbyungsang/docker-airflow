```
python3 -m venv sandbox
source sandbox/bin/activate

pip install apache-airflow==2.0.0b3
```

### Major Configurations (airflow.cfg)
```
# dags folder 
dags_folder = /opt/airfow/dags

# executor 
executor = SequentialExcutor

# sql_alchemy_conn 
sql_alchemy_conn = sqlite:////opt/airflow/airflow.db

# parallelism and concurrency
parallelism = 32
dag_concurrency = 16
max_active_runs_per_dag

```