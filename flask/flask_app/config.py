#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/11
# @Author  : kingsley kwong
# @Site    :
# @File    : config.py
# @Software: flask_app
# @Function:
import os
from kombu import Queue,Exchange
basedir = os.path.abspath(os.path.dirname(__file__))




class BaseConfig(object):
    DEBUG = False
    TESTING = False
    USERNAME = 'admin'
    PASSWORD = 'admin'
    SECRET_KEY = os.urandom(24)
    #SESSION_COOKIE_NAME = ''
    #SESSION_COOKIE_DOMAIN = ''
    #SESSION_COOKIE_PATH = ''
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    LOGGER_NAME = ''
    #CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI='sqlite://:memory:'
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # DataBase_Config
    DB_URL = ""
    DB_USER = ""
    DB_PASSWD = ""
    DB_NAME = ""

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = ''

class DevelopConfig(BaseConfig):
    DEBUG = True
    #redis
    REDIS_HOST = '192.168.1.172'
    REDIS_PORT = 6379
    REDIS_DB = 0

    #mongodb
    MONGODB_URI = 'mongodb://localhost:27017/test'

    #celery
    CELERY_INCLUDE = ('flask_app.tasks.files',
                      'flask_app.tasks.web',
                      'flask_app.tasks.mega_task',)

    CELERY_BROKER_URL = 'redis://192.168.1.172:6379/1'
    CELERY_RESULT_BACKEND = 'redis://192.168.1.172:6379/2'
    CELERYD_CONCURRENCY = 20
    CELERYD_PREFETCH_MULTIPLIER = 4
    CELERYD_TASK_TIME_LIMIT = 3600
    CELERY_TASK_DEFAULT_QUEUE = 'default'
    CELERY_ROUTES=(
                      {'flask_app.tasks.files.*':{'queue': 'files',
                                      'exchange':'files',
                                      'exchange_type':'direct',
                                      'routing_key':'files'}},

                      {'flask_app.tasks.mega_task.*': {'queue': 'mega_task',
                                                   'exchange': 'mega_task',
                                                   'exchange_type': 'direct',
                                                   'routing_key': 'mega_task'}},

                      {'flask_app.tasks.web.*':{'queue': 'web',
                                    'exchange':'web',
                                    'exchange_type':'direct',
                                    'routing_key':'web'}},)

    CSRF_ENABLED = True
    # DataBase_Config
    DB_URL = "192.168.1.172"
    DB_PORT = "3306"
    DB_USER = "kingsley"
    DB_PASSWD = "123456"
    DB_NAME = "test"
    #sqlORM
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s:%s/%s?unicode" %(DB_USER,DB_PASSWD,DB_URL,DB_PORT,DB_NAME)
    SQLALCHEMY_POOL_TIMEOUT = 5

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ''

config = {
    'product':ProductionConfig,
    'develop':DevelopConfig,
    'testing':TestingConfig
}

