from celery.task import task
from django.conf import settings
from models import Log

@task
def add(x=2, y=2):
    print 'add'
    return x + y

@task
def test_default():
    """
    level = models.CharField(max_length=128)
    msg = models.TextField()
    source = models.CharField(max_length=128, blank=True)
    host = models.CharField(max_length=200, blank=True, null=True)
    """
    print 'default task'
    return Log.objects.create(level='TEST', msg='Celery logging test', source='TEST', host='TEST')


@task(queue=settings.CELERY_QUEUE_BIGTASK)
def test_bigtasks():
    print 'bigtasks'
    return Log.objects.create(level='TEST BIGTASKS', msg='Celery logging BIGTASKS', source='BIGTASKS', host='BIGTASKS')


@task(queue=settings.CELERY_QUEUE_IPM)
def test_ipm():
    print 'ipm'
    return Log.objects.create(level='TEST IPM', msg='Celery logging IPM', source='IPM', host='IPM')


@task(queue=settings.CELERY_QUEUE_CPOS_OI)
def test_cpos_oi():
    print 'cpos oi'
    return Log.objects.create(level='TEST CPOS_OI', msg='Celery logging CPOS_OI', source='CPOS_OI', host='CPOS_OI')


@task(queue=settings.CELERY_QUEUE_CPOS_CLARO)
def test_cpos_claro():
    print 'cpos claro'
    return Log.objects.create(level='TEST CPOS_CLARO', msg='Celery logging CPOS_CLARO', source='CPOS_CLARO', host='CPOS_CLARO')


@task(queue=settings.CELERY_QUEUE_CPOS_TIM)
def test_cpos_tim():
    print 'cpos tim'
    return Log.objects.create(level='TEST CPOS_TIM', msg='Celery logging CPOS_TIM', source='CPOS_TIM', host='CPOS_TIM')


@task(queue=settings.CELERY_QUEUE_FLOWBOT)
def test_cpos_flowbot():
    print 'cpos tim'
    return Log.objects.create(level='TEST FLOWBOT', msg='Celery logging FLOWBOT', source='FLOWBOT', host='FLOWBOT')


@task(queue=settings.CELERY_QUEUE_DATA_IMPORTER)
def test_data_importer():
    print 'data import'
    return Log.objects.create(level='TEST DATA_IMPORTER', msg='Celery logging DATA_IMPORTER', source='DATA_IMPORTER', host='DATA_IMPORTER')


def test_celery():
    test_default.delay()
    test_bigtasks.delay()
    test_ipm.delay()
    test_cpos_oi.delay()
    test_cpos_claro.delay()
    test_cpos_tim.delay()
    test_data_importer.delay()
    print 'ok'
