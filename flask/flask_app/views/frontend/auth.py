#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    : 
# @File    : 
# @Software: 
# @Function:



from flask import Blueprint, request, jsonify
from flask_app import app

from flask_app.views._md5 import MD5
from flask_app.models.auth import User





auth = Blueprint('auth', __name__, url_prefix='/auth')

re_dict = lambda str1,str2,str3,str4=None:{'code':str1,'state':str2,'statement':str3,'privilege':str4}

@auth.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		data = request.get_json()
		users = User.query.filter_by(name=data['username']).all()
		psw = MD5(data['password'])
		if not users :
			return jsonify(re_dict('02','False','user not exists'))
		else:
			user = users[0]

		if str(user.name) == str(data['username']) and str(user.password) == str(psw):
			if int(user.privileges) == 1:
				return jsonify(re_dict('01','True','adminstrator login in','1'))
			elif int(user.privileges) == 2:
				return jsonify(re_dict('01', 'True','guest login in' ,'2'))
			else:
				return jsonify(re_dict('04', 'False', 'Role exception'))
		else:
			return jsonify(re_dict('03','False','password incorrect'))


@auth.route('/register',methods=['GET','POST'])
def register():
	if request.method == 'POST':
		data = request.get_json()
		users = User.query.filter_by(name = data['username']).all()
		if users:
			return jsonify(re_dict('02','False','user exists'))
		else:
			psw = MD5(data['password'])
			u = User(name=data['username'],password=psw,privileges='2')
			u.add()
			u.commit()
			add_user = User.query.filter_by(name = data['username']).first()
			if str(add_user.name) == str(data['username']) and str(add_user.password) == str(psw):
				return jsonify(re_dict('01','True','User Added Successfully!'))
			else:
				return jsonify(re_dict('03','False','User Added Error,please check your connection of database!'))

@auth.route('/testsql',methods=['GET','POST'])
def testsql():
	if request.method == 'GET':
		user = User.query.filter_by(name='aaa').first()
		#app.logger.debug(user)
		return "testsql"