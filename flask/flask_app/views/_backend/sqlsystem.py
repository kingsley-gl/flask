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
from ._forms import TableForm
from math import ceil

sqlsystem = Blueprint('sqlsystem', __name__)
#header register
__func = [
			# {function_name:chinese_name},
			{'detail':'详情'},
		  	{'db_list':'数据库列表'},
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
		error = None
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		# form = PageForm(request.form)
		tables = []
		pages = None #total page
		page = request.args.get('page', 1, type=int)
		perpage = 10
		try:
			# if form.validate_on_submit():
			# 	perpage = form.PerPage.data

			total = _db.engine.execute('''select count(*) from information_schema.tables 
											where table_schema = "%s";''' %_config['DB_NAME'])
			total = total.first()[0]
			data = _db.engine.execute('''select table_name,table_rows,create_time,table_comment 
								from information_schema.tables 
								where table_schema = "%s" 
								order by create_time limit %s offset %s ;''' %(_config['DB_NAME'],perpage,(page-1)*perpage))
			pages = int(ceil(float(total) / float(perpage)))

			for item in data.fetchall():
				table = {}
				table['name'] = item[0]
				table['rows'] = item[1]
				table['create_time'] = item[2]
				table['comment'] = item[3]
				tables.append(table)
		except Exception as e:
			error = e
		return render_template('sqlsystem/db_list.html',
							   headers=__func,
							   module='sqlsystem',
							   error = error,
							   tables=tables,
							   # form=form,
							   pages=pages,
							   page=page)
	except KeyError:
		return redirect(url_for('home.login'))

@sqlsystem.route('/opration',methods=['GET','POST'])
def opration():
	error = None
	form = TableForm(request.form)
	tbname = request.args.get('tbname',None,type=str)
	page = request.args.get('page', 1, type=int)
	perpage = 10
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		try:
			total = _db.engine.execute('''select count(*) from %s''' %tbname)
			total = total.first()[0]
			pages = int(ceil(float(total) / float(perpage)))
			column = _db.engine.execute('''show columns from %s''' %tbname)
			data = _db.engine.execute('''select * from %s order by id limit %s offset %s''' %(tbname,perpage,(page-1)*perpage))
			TableForm.create_field('name','data_required')

			for item in column.fetchall():
				print(item)

			for a,b,c,d in data.fetchall():
				print(a,b,c,d)
		except Exception as e:
			error = e
		return render_template('sqlsystem/opration.html',
							   headers=__func,
							   module='sqlsystem',
							   error=error,
							   page=page,
							   pages=pages)
	except KeyError:
		return redirect(url_for('home.login'))