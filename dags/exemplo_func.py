from time import sleep
from airflow.decorators import dag, task
from datetime import datetime

@dag(dag_id="primeira_dag", description="criando uma dag pela primeira vez", start_date=datetime(2024, 1, 1), schedule="0 0 * * *", catchup=False)
def pipeline():

    @task
    def primeira_atividade():
        print("Primeira atividade rodou com sucesso")
        sleep(2)
    @task
    def segunda_atividade():
        print("Segunda atividade rodou com sucesso")
        sleep(2)
    @task
    def terceira_atividade():
        print("Terceira atividade rodou com sucesso")
        sleep(2)

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()

    t1 >> t2 >> t3

pipeline()