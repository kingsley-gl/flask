#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/28
# @Author  : kingsley kwong
# @Site    :
# @File    : sqlsystem.py
# @Software: flask_app
# @Function:

from flask import *
from flask_app import _config,_db

sqlsystem = Blueprint('sqlsystem', __name__)
#header register
__func = [
			# {function_name:chinese_name},
			{'detail':'xiangqing'},
		  	{'db_list':'shujukuliebiao'},
			{'opration':'shujukubiaodan'}
		]


@sqlsystem.route('/detail',methods=['GET','POST'])
def detail():
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		db_user = _config['DB_USER']
		db_password = _config['DB_PASSWD']
		db_ip = _config['DB_URL']
		db_port = _config['DB_PORT']
		db_name = _config['DB_NAME']
		error = None
		try:
			_db.engine.table_names()
			db_state = True
		except Exception as e:
			db_state = False
			error = e
		return render_template('sqlsystem/detail.html',
							   headers = __func,
							   module='sqlsystem',
							   db_state = db_state,
							   db_user=db_user,
							   db_password=db_password,
							   db_ip=db_ip,
							   db_port=db_port,
							   db_name=db_name,
							   error=error)
	except KeyError:
		return redirect(url_for('home.login'))

@sqlsystem.route('/db_list',methods=['GET','POST'])
def db_list():
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		error = None
		tables = []
		try:
			for item in (_db.engine.execute('select table_name,table_rows from information_schema.tables where table_schema = "test";')):
				print(item)
			# for
			# 	table = {}
			#
			#
			# 	tables.append(table)
		except Exception as e:
			error = e
		return render_template('sqlsystem/db_list.html',
							   headers=__func,
							   module='sqlsystem',
							   error = error,
							   tables=tables)
	except KeyError:
		return redirect(url_for('home.login'))

@sqlsystem.route('/opration',methods=['GET','POST'])
def opration():
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		return render_template('sqlsystem/opration.html', headers=__func, module='sqlsystem')
	except KeyError:
		return redirect(url_for('home.login'))