from .base import *
import dj_database_url

ENVIRONMENT = 'production'
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES['default'] = dj_database_url.config(
    default='postgres://fyljteumxrotqu:aebd2c01a0eecb4d0e0c19f66e9c6de850505c21a1ca1b4572e78bacb8f7e66f@ec2-107-20-188-239.compute-1.amazonaws.com:5432/d7hqf9bcb3o3dt'
)