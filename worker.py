
from celery import  Celery


t=Celery('my_tasks',broker="redis://localhost:8000",backend="redis://localhost:8000")

t.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)


@t.task("excute")
def excute_sql():
    pass


