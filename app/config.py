import os

DEBUG = True

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://preturi:preturi@localhost/preturi'
SECRET_KEY = 'my_key'
WHOOSH_BASE = 'search.db'
MAX_SEARCH_RESULTS = 150

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'ENGINE': 'mysql',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
    }
else:
    DATABASES = {
        'ENGINE': 'mysql',
        'NAME': 'preturi',
        'USER': 'preturi',
        'PASSWORD': 'preturi',
        'HOST': 'localhost',
        'PORT': '3306',
    }

SQLALCHEMY_DATABASE_URI = \
    '{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}'.format(
        dialect=DATABASES['ENGINE'],
        driver='pymysql',
        username=DATABASES['USER'],
        password=DATABASES['PASSWORD'],
        host=DATABASES['HOST'],
        port=DATABASES['PORT'],
        database=DATABASES['NAME'])
#dialect+driver://username:password@host:port/database