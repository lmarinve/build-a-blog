from flask import render_template, Flask, request, redirect, session, url_for, flash
from handymia import app, insert
from handymia.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    welcome = {'message': 'Welcome to HandyMia'}
    return render_template("main.html", title='Home', welcome=welcome)


@app.route('/login', methods=['GET', 'POST'])
def login():
    #insert.insertar()
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.username.data
        '''Flask('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))'''
        return redirect(url_for('/index'))
    return render_template('login.html', title='Sign in', form=form, name=session.get('name'))


tasks = []
@app.route('/todos', methods=['GET', 'POST'])
def todos():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
    return render_template("todos.html", title='Get It Done!', tasks=tasks)


