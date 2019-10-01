from flask import render_template, flash, redirect
from handymia import app
from handymia.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    welcome = {'message': 'Welcome to HandyMia'}
    return render_template("main.html", title='Home', welcome=welcome)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign in', form=form)
