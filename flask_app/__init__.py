#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    : 
# @File    : views.__init__.py
# @Software: flask_app
# @Function:

from flask import Flask
from flask_app.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from pymongo import MongoClient
from flask_cors import *
from celery import Celery
import redis
from flask_pymongo import PyMongo
import datetime
import psutil
import types

GB = 1024.0**3

app = Flask(__name__,static_folder='static',static_url_path='')
CORS(app)
app.config.from_object(config['develop2'])
_config = app.config
pcm = psutil.virtual_memory()
__all__=['doc','log',
         'models','static',
         'templates','views',
         'app','api',
         'config','task',
         'cel_manage','logger','worker']



def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

def logger(func):
    def inner(*args,**kwargs):
        app.logger.debug("%s flask debug args: %s" %(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),args))
        print("Total Memory:%s GB,Available Memory:%s GB" %(pcm.total/GB,pcm.available/GB))
        print("Used Memory:%s GB,Memory Percentage:%s %%" %(pcm.used/GB,pcm.percent))
        print("%s flask debug in function: %s %s" %(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                   func.__name__,args))
        return func(*args,**kwargs)
    return inner
#connection needs to optimize
try:
    _db = SQLAlchemy(app)
    _cel = make_celery(app)
    _api = Api(app)
except Exception as e:
    app.logger.error(e)
try:
    _mongo = MongoClient(app.config['MONGO_URI'])
except Exception as e:
    app.logger.error(e)
try:
    _pool = redis.ConnectionPool(host=app.config['REDIS_HOST'],
                                  port=app.config['REDIS_PORT'],
                                  db=app.config['REDIS_DB'])
except Exception as e:
    app.logger.error(e)
try:
    import flask_app.api
    from flask_app.views import *
    #auto blueprint
    for module in dir(flask_app.views):
        if module[0] == '_':
            continue
        app.register_blueprint(eval(module + '.' +module))
except Exception as e:
    app.logger.error(e)





