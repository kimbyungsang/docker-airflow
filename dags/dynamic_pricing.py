from airflow.models import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.microsoft.mssql.operators.mssql import MsSqlOperator
from airflow.providers.odbc.hooks.odbc import OdbcHook

from datetime import datetime
from pandas import json_normalize
import json
import pyodbc

default_args = {
    'start_date':datetime(2020,1,1)
}

def _get_data():
    query = ''' select top 10 from rentorder'''
    mssql_hook = OdbcHook()
    connection = mssql_hook.get_conn()
    cursor = connecion.cursor()
    cursor.execute(query)
    sources = cursor.fetchall()
    for source in sources:
        print("{0} and  {1}".format(source[0], source[1]))
    return sources


with DAG('dynamic_pricing', 
        schedule_interval='@daily',
        default_args=default_args) as dag:

    get_data_from_db = MsSqlOperator(
        task_id='get_data_from_db',
        mssql_conn_id='mssql_source_db',
        sql='./dynamic_pricing.sql',
        database='CACAOCAR',
        autocommit=False
    )

    get_data_from_mssql = PythonOperator(
        task_id ='get_data_from_mssql',
        python_callable=_get_data
    )

    task4 = BashOperator(
        task_id = 'task4',
        bash_command='echo hello'
    )

    get_data_from_db  >> get_data_from_mssql >> task4
