#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    :
# @Software:
# @Function:
import os
basedir = os.path.abspath(os.path.dirname(__file__))
#DataBase_Config
DB_URL = "192.168.1.172:3306"
DB_USER = "kingsley"
DB_PASSWD = "123456"
DB_NAME = "test"


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    #SESSION_COOKIE_NAME = ''
    #SESSION_COOKIE_DOMAIN = ''
    #SESSION_COOKIE_PATH = ''
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    LOGGER_NAME = 'Cesium Server'
    #SERVER_NAME = '192.168.1.144:8000'
    SQLALCHEMY_DATABASE_URI='sqlite://:memory:'
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = ''

class DevelopConfig(BaseConfig):
    DEBUG = True
    REDIS_HOST = '192.168.1.172'
    REDIS_PORT = 6379
    REDIS_DB = 0
    MONGODB_URI = 'mongodb://localhost:27017/test'
    CELERY_BROKER_URL = 'redis://192.168.1.172:6379/1'
    CELERY_RESULT_BACKEND = 'redis://192.168.1.172:6379/2'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + DB_USER + ":" + DB_PASSWD + "@" + DB_URL + "/" + DB_NAME + "?unicode"

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ''

config = {
    'product':ProductionConfig,
    'develop':DevelopConfig,
    'testing':TestingConfig
}

