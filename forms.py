from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, RadioField
from wtforms.validators import DataRequired, Email, Length

##############################################################################
# Forms
############################################################################## 

class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    address = StringField('Address')
    lat = StringField('Latitude', validators=[DataRequired()])
    long = StringField('Latitude', validators=[DataRequired()])
    method = RadioField('Notification Method')
    cellphone = IntegerField('Cellphone Number', validators=[DataRequired()])
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    
class EditProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    lat = StringField('Latitude', validators=[DataRequired()])
    long = StringField('Longitude', validators=[DataRequired()])
    method = RadioField('Notification Method')
    cellphone = IntegerField('Cellphone Number', validators=[DataRequired()])
 
     