#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, url_for, render_template, request, flash, \
    session, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'sql6428478'
app.config['MYSQL_PASSWORD'] = 'Tk3jBdaXtt'
app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql6428478'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
app.config['CACHE_TYPE'] = 'null'


@app.route('/')
def mainpage():
    data = session.get('username')
    if not data:
        data = 'NOT LOGGED IN'
    return render_template('index.html', data=data)


@app.route('/login', methods=['GET', 'POST'])
def loginpage():
    if request.method == 'POST' and 'username' in request.form \
        and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = '%s' AND password = '%s'"
                     % (username, password))
        data = cur.fetchone()
        if data:
            session['logged'] = True
            session['username'] = username
            data = 'Successfully logged in!'
            return render_template('login.html', data=data)
        else:
            data = 'Invalid credentials'
            return render_template('login.html', data=data)
    else:
        if session.get('logged') == True:
            return render_template('no.html')
        else:
            return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def registerpage():
    if request.method == 'POST' and 'username' in request.form \
        and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = '%s' AND password = '%s'"
                     % (username, password))
        data = cur.fetchone()
        if not data:
            cur.execute("INSERT INTO users (email, password, strikes) VALUES ('%s', '%s', 0)"
                         % (username, password))
            mysql.connection.commit()
            data = 'Account created'
            return render_template('register.html', data=data)
        else:
            data = 'Email already exists!'
            return render_template('register.html', data=data)
    else:
        data = ''
        return render_template('register.html', data=data)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if session.get('logged'):
        if session['logged']:
            cur = mysql.connection.cursor()
            cur.execute("SELECT strikes FROM users WHERE email = '%s'"
                        % session['username'])
            strikes = cur.fetchone()
            if strikes:
                return render_template('profile.html',
                        strikes=strikes['strikes'])
        else:
            return redirect(url_for('mainpage'))
    else:
        return redirect(url_for('mainpage'))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('logged', None)
    session.pop('username', None)
    return redirect(url_for('mainpage'))

if __name__ == '__main__':
    app.secret_key = 'blehblehbleh123'
    app.SESSION_TYPE = 'filesystem'
    app.run(debug=True)
