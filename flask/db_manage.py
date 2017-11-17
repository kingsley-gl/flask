#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    :
# @Software:
# @Function:

from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_app import _db,app

manager = Manager(app)
migrate = Migrate(app,_db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()


