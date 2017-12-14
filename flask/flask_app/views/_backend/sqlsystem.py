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
import types

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
		perpage = 15
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
							   pages=pages,
							   page=page)
	except KeyError:
		return redirect(url_for('home.login'))

@sqlsystem.route('/opration',methods=['GET','POST'])
def opration():
	error = None

	tbname = request.args.get('tbname',None,type=str)
	page = request.args.get('page', 1, type=int)
	perpage = 15
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		try:
			total = _db.engine.execute('''select count(*) from %s''' %tbname)
			total = total.first()[0]
			pages = int(ceil(float(total) / float(perpage)))
			print(pages)
			column = _db.engine.execute('''show columns from %s''' %tbname)
			data = _db.engine.execute('''select * from %s order by id limit %s offset %s''' %(tbname,perpage,(page-1)*perpage))

			#meta table class
			locals()[tbname] = type(tbname,(TableForm,),{})

			#table columns add
			col_name = []
			for item in column.fetchall():
				col_name.append(item[0])
				if (set(item[1]) & set('int')) == set('int'):
					locals()[tbname].create_field(item[0], 'IntegerField')
				elif (set(item[1]) & set('varchar')) == set('varchar'):
					locals()[tbname].create_field(item[0], 'StringField')
				elif (set(item[1]) & set('datetime')) == set('datetime'):
					locals()[tbname].create_field(item[0], 'DateTimeField')
				elif (set(item[1]) & set('date')) == set('date'):
					locals()[tbname].create_field(item[0], 'DateField')

			forms = []
			tbkeys = ''
			tbvalues = ''
			#records add
			for value in data.fetchall():
				locals()['form_id_'+str(value[0])] = locals()[tbname](request.form)
				if locals()['form_id_'+str(value[0])].validate_on_submit():
					for key in locals()['form_id_'+str(value[0])].data.keys():
						if key == 'csrf_token':
							continue
						tbkeys += key + ','
						if type(locals()['form_id_' + str(value[0])].data[key]) is type(1):
							tbvalues += str(locals()['form_id_' + str(value[0])].data[key]) + ','
						elif type(locals()['form_id_' + str(value[0])].data[key]) is type('a'):
							tbvalues += '"'+str(locals()['form_id_' + str(value[0])].data[key])+'"' + ','
					tbkeys = tbkeys[:-1]
					tbvalues = tbvalues[:-1]
					sql = '''replace into %s(%s) values (%s);''' %(tbname,tbkeys,tbvalues)
					_db.engine.execute(sql)
					return redirect(url_for('sqlsystem.opration',page=page,tbname=tbname))
				else:
					ret = dict(zip(col_name,value)) # zip two list in dict
					for key in ret.keys():
						locals()['form_id_' + str(value[0])].__dict__[key].data = ret[key]
					forms.append(locals()['form_id_' + str(value[0])])

		except Exception as e:
			error = e
		return render_template('sqlsystem/opration.html',
							   headers=__func,
							   module='sqlsystem',
							   error=error,
							   page=page,
							   pages=pages,
							   tbname=tbname,
								forms=forms)
	except KeyError:
		return redirect(url_for('home.login'))

@sqlsystem.route('/insertRow',methods=['GET','POST'])
def insert_row():
	if request.method == 'POST':
		tbname = request.args.get('tbname', None, type=str)
		json_data = {key: dict(request.form)[key][0] for key in dict(request.form)}
		rowkeys = ''
		rowvalues = ''
		for key in json_data.keys():
			rowkeys += key + ','
			rowvalues +=  json_data[key] + ','
		try:
			sql = '''insert into %s(%s) values (%s)''' %(tbname,rowkeys[:-1],rowvalues[:-1])
			print(sql)
			_db.engine.execute(sql)
		except Exception as e:
			return e
		return 'insert data success'

@sqlsystem.route('/deleteRow',methods=['GET','POST'])
def delete_row():
	if request.method == 'POST':
		tbname = request.args.get('tbname', None, type=str)
		json_data = {key: dict(request.form)[key][0] for key in dict(request.form)}
		print(json_data)
		sql = '''delete from %s where id = %s''' %(tbname,json_data['id'])
		print(sql)
		try:
			_db.engine.execute(sql)
			return 'data delete success'
		except Exception as e:
			return redirect('sqlsystem.opration',error=e)