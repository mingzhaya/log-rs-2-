from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class MapDropForm(FlaskForm):
    m0g0r0 = SubmitField('0, 0, 0')
    m1g0r0 = SubmitField('1, 0, 0')
    m2g0r0 = SubmitField('2, 0, 0')  
    m0g1r0 = SubmitField('0, 1, 0')  
    m1g1r0 = SubmitField('1, 1, 0')  
    m2g1r0 = SubmitField('2, 1, 0')  
    m0g0r1 = SubmitField('0, 0, 1')  
    m1g0r1 = SubmitField('1, 0, 1')  
    m2g0r1 = SubmitField('2, 0, 1')     
    m0g1r1 = SubmitField('0, 1, 1')  
    m1g1r1 = SubmitField('1, 1, 1')  
    m2g1r1 = SubmitField('2, 1, 1')
    delete = SubmitField('Delete last')
