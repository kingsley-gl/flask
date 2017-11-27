#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    : 
# @File    : 
# @Software: 
# @Function:

from flask import *
from flask_app import _config
from .import __modules

home = Blueprint('home', __name__)



@home.route('/',methods=['GET','POST'])
def login():
	username_error = None
	password_error = None
	if request.method == 'POST':
		if request.form['username'] != _config['USERNAME']:
			username_error = 'invalid user'
		elif request.form['password'] != _config['PASSWORD']:
			password_error = 'invalid password'
		else:
			session['logged_in'] = True
			return redirect(url_for('home.homepage'))
	return render_template('login/login.html', username_error=username_error, password_error=password_error)

@home.route('/logout',methods=['GET','POST'])
def logout():
	session.pop('loggen_in',None)
	return redirect(url_for('home.login'))

@home.route('/homepage',methods=['GET','POST'])
def homepage():
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		return render_template('home/home.html', headers = __modules)
	except KeyError:
		return redirect(url_for('home.login'))




