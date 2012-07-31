# List of modules to import when celery starts.
CELERY_IMPORTS = ("burn.tasks", )

BROKER_HOST = "192.168.134.147"
BROKER_PORT = 5672
BROKER_VHOST = "ubuntumq"
BROKER_USER = "ubuntu"
BROKER_PASSWORD = "ubuntu"

## Worker settings
## If you're doing mostly I/O you can have more processes,
## but if mostly spending CPU, try to keep it close to the
## number of CPUs on your machine. If not set, the number of CPUs/cores
## available will be used.
CELERYD_CONCURRENCY = 8

# Where to chdir at start.
# CELERYD_CHDIR="/home/valdergallo/www/study-celery/study"

# Extra arguments to celeryd
# CELERYD_OPTS="--time-limit=14000 -S -E -B"  # load celerymon, celerybeat, celeryevent

# create log and daemon process
#CELERYD_LOG_FILE="/tmp/celery.log"
#CELERYD_PID_FILE="/tmp/celery.pid"

# Extra arguments to celerybeat
# CELERYBEAT_OPTS="--schedule=/tmp/celerybeat-schedule"

# Set annotate for time control
CELERY_DEFAULT_QUEUE = "default"
CELERY_DEFAULT_ROUTING_KEY = "default"
CELERY_DEFAULT_EXCHANGE_TYPE = "fanout"

CELERY_QUEUES = {
    "default": {
        "exchange": "default",
        "binding_key": "default",
    },
    "flowbot": {
        "exchange": "flowbot",
        "binding_key": "flowbot.#",
    },
    "data_importer": {
        "exchange": "data_importer",
        "binding_key": "data_importer.#",
    },
    "cpos_oi": {
        "exchange": "cpos_oi",
        "binding_key": "cpos_oi.#",
    },
    "cpos_claro": {
        "exchange": "cpos_claro",
        "binding_key": "cpos_claro.#",
    },
    "cpos_tim": {
        "exchange": "cpos_tim",
        "binding_key": "cpos_tim.#",
    },
    "ipm": {
        "exchange": "ipm",
        "binding_key": "ipm.#",
    },
    "bigtask": {
        "exchange": "bigtask",
        "binding_key": "bigtask.#",
    },
}

##########################################################
# Celery
# RabitQM Broker configuration for Celery
# http://ask.github.com/celery/getting-started/first-steps-with-django.html
# CELERY_SEND_TASK_ERROR_EMAILS = True
CELERYD_PREFETCH_MULTIPLIER = 1
CELERYD_MAX_TASKS_PER_CHILD = 1

CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"


##########################################################
# Celery Queue
CELERY_QUEUE_BIGTASK = 'bigtask'
CELERY_QUEUE_IPM = 'ipm'
CELERY_QUEUE_CPOS_OI = 'cpos_oi'
CELERY_QUEUE_CPOS_CLARO = 'cpos_claro'
CELERY_QUEUE_CPOS_TIM = 'cpos_tim'
CELERY_QUEUE_FLOWBOT = 'flowbot'
CELERY_QUEUE_DATA_IMPORTER = 'data_importer'

from datetime import timedelta


CELERYBEAT_SCHEDULE = {
        'runs-every-30-seconds': {
        'task': 'burn.tasks.add',
        'schedule': timedelta(seconds=10),
        'args': (16, 16)
    },
}


import djcelery
djcelery.setup_loader()
