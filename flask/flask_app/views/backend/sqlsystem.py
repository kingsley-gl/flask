#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    :
# @Software:
# @Function:

from flask import *
from .import __modules
sqlsystem = Blueprint('sqlsystem', __name__)

@sqlsystem.route('/sqlsystem',methods=['GET','POST'])
def sqlsystem():
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		return render_template('sqlsystem/sql_system.html', headers = __modules)
	except KeyError:
		return redirect(url_for('home.login'))