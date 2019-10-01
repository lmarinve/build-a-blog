from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=3,
                                        message='Little short'), Length(max=20, message=u'too long'),
                                        validators.Regexp('^[A-Za-z]*$', message='Must have only letters')])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    email = StringField('Email Address', [validators.Length(min=3, message=u'Little short'), Length(max=20,
                                          message=u'too long'), Email(message='not a valid email address')])
    submit = SubmitField('Sign In')
