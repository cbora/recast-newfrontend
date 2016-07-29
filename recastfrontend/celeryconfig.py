from datetime import timedelta
from recastfrontend.frontendconfig import config as frontendconf
from recastsearch.config import Config

BROKER_URL = frontendconf['REDISURL']
CELERY_RESULT_BACKEND = frontendconf['REDISURL']
elasticsearchconfig = Config(
    HOST=frontendconf['ELASTIC_SEARCH_URL'],
    AUTH=frontendconf['ELASTIC_SEARCH_AUTH'],
    INDEX=frontendconf['ELASTIC_SEARCH_INDEX']
    )
    
CELERYBEAT_SCHEDULE = {
  'add-every-30-seconds': {
    'task': 'asynctasks.sync_elasticsearch',
    'schedule': timedelta(seconds=30),
    'args': (elasticsearchconfig)
    },
  }

CELERY_TIMEZONE = 'UTC'
