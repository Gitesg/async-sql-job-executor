
from celery import Celery

import  redis
import  asyncpg
import asyncio



t=Celery('my_tasks',broker="redis://localhost:6379/0",backend="redis://localhost:6379/1")

t.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)


async def run_qurey(r):



    conn = await asyncpg.connect(
    host="localhost",
    database="mydbx",
    user="admin",
    password="admin@1234"
)

    print(conn)

    x=await  conn.fetch(r)
    await conn.close()

    return [ dict(row) for row in x]




@t.task(name="execute_sql")
def execute_sql():
    with open("queris.sql","r") as r:

        x=r.read().strip()

    loop=asyncio.get_event_loop()
    res=loop.run_until_complete(run_qurey(x))
    return  res










