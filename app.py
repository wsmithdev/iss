import os
from crypt import methods
from flask import Flask, redirect, render_template, g, session
from sqlalchemy.exc import IntegrityError
from dotenv import load_dotenv
import threading
from models import db, connect_db, User, Location, Notification
from forms import SignUpForm, LoginForm, EditProfileForm
from iss_location import get_ISS_location
from continuous import continuous_call


# Environment variables
load_dotenv()

# App setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "postgresql:///iss-tracker")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "secretkey123")


# Connect to db
connect_db(app)

newThread = threading.Thread(target=continuous_call)
newThread.start()

##############################################################################
# User auth
##############################################################################

CURR_USER_KEY = "curr_user"

@app.before_request
def add_user_to_g():
    
    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else:
        g.user = None
        
def do_login(user):
    session[CURR_USER_KEY] = user.id
    
def do_logout():
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
    



##############################################################################
# ROUTES
##############################################################################

####################
# Navigation Routes
####################

# Home route
@app.route('/')
def root():
    return redirect('/iss')

# ISS route
@app.route('/iss')
def iss():
    iss_location = get_ISS_location()
    return render_template('home.html', iss_location=iss_location)

####################
# Auth Routes
####################

# Sign up 
#############
@app.route('/signup', methods=["GET", "POST"])
def signup():
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
         
    form = SignUpForm()
    notification_method_choices = [(n_m.id, n_m.method) for n_m in Notification.query.all()]
    form.method.choices = notification_method_choices
    
    if form.validate_on_submit():
        print("Trying to sign up")
        # Save location to database
        location = Location.add_location(
            lat=form.lat.data,
            long=form.long.data
        )
        db.session.commit()

        # Save user to database
        user = User.signup(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=form.password.data,
            location_id=location.id,
            notification_method_id=form.method.data,
            cellphone=form.cellphone.data
        )
        db.session.commit()
        do_login(user)
        return redirect('/')
    else:
        print("Not trying to sign up")
        return render_template('auth/signup.html', form=form, button='Sign up')
       
 
 # Login
 ########
@app.route('/login', methods=["GET", "POST"])
def login():
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.authenticate(
            email=form.email.data,
            password=form.password.data
        )
        
        if user:
            do_login(user)
            return redirect('/')
    return render_template('auth/login.html', form=form)
  
# Logout
#########
@app.route('/logout')
def logout():
    do_logout()
    return redirect('/')


####################
# User Routes
####################

# Edit profile 
##########
@app.route('/profile', methods=["GET", "POST"])
def edit_profile():
    user_id = g.user.id
    
    # Get location
    location = Location.query.get_or_404(g.user.location_id)
    # Add data to global user
    g.user.lat = location.lat
    g.user.long = location.long
    
    # Get user
    user = User.query.get_or_404(g.user.id)
  
    user.method = user.notification_method_id 
    form = EditProfileForm(obj=user)
    notification_method_choices = [(n_m.id, n_m.method) for n_m in Notification.query.all()]
    form.method.choices = notification_method_choices
    
    if form.validate_on_submit():
               
        # Save location to database
        location.lat = form.lat.data
        location.long = form.long.data
        db.session.add(location)
        db.session.commit()
        
        # Save user data to database
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email = form.email.data
        user.notification_method_id = form.method.data
        user.cellphone = form.cellphone.data
        db.session.add(user)
        db.session.commit()
        g.user.id = user.id
   
        return redirect('/')
    else:
        return render_template('users/edit.html', form=form, user_id=user_id, button="Save")
    

# Delete profile 
#################
@app.route('/profile/delete/<int:user_id>')
def delete_user(user_id):
    
    return redirect('/')







