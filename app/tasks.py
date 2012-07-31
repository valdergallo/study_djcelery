from celery import task
from celery.contrib import rdb
from datetime import datetime

@task()
def add(x, y):
    result = x + y
    print result, datetime.now()
    #rdb.set_trace()  # <- set breakpoint
    return result
