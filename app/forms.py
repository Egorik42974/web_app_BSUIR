from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import DataRequired


class catForm(FlaskForm):
    nameField = StringField('nameField')


class LoginForm(FlaskForm):
    loginField = StringField('loginField', validators=[DataRequired()])
    passwordField = PasswordField('passwordField', validators=[DataRequired()])


class RegForm(FlaskForm):
    usernameField = StringField('usernameField', validators=[DataRequired()])
    loginField = StringField('loginField', validators=[DataRequired()])
    passwordField = PasswordField('passwordField', validators=[DataRequired()])
    passwordConfirmField = PasswordField('passwordConfirmField', validators=[DataRequired()])
