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
from ._forms import PageForm
from math import ceil

sqlsystem = Blueprint('sqlsystem', __name__)
#header register
__func = [
			# {function_name:chinese_name},
			{'detail':'详情'},
		  	{'db_list':'数据库列表'},
			{'opration':'数据库表单'}
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
def db_list(page=1):
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		form = PageForm(request.form)
		error = None
		length = None
		rows=None
		tables = []
		perpage = form.PerPage.data


		try:
			if form.validate_on_submit():
				perpage=form.PerPage.data

			data = _db.engine.execute('''select table_name,table_rows,create_time,table_comment 
								from information_schema.tables 
								where table_schema = "%s";''' %_config['DB_NAME'])
			page = request.args.get('page',1,type=int)
			for item in data.fetchall()[(page-1)*perpage:page*perpage]:
				table = {}
				table['name'] = item[0]
				table['rows'] = item[1]
				table['create_time'] = item[2]
				table['comment'] = item[3]
				tables.append(table)
			rows = data.rowcount
			length = int(data.rowcount / perpage) + 1
		except Exception as e:
			error = e
		return render_template('sqlsystem/db_list.html',
							   headers=__func,
							   module='sqlsystem',
							   error = error,
							   tables=tables,
							   length=length,
							   rows=rows,
							   form=form)
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