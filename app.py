from flask import Flask, redirect, render_template, g, session
from sqlalchemy.exc import IntegrityError
#from decouple import config
from models import db, connect_db, User
from forms import SignUpForm, LoginForm

# App setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///iss-tracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "config('DB_SECRET_KEY', default='')"


# Connect to db
connect_db(app)

# Create tables
db.create_all()

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

# Home route
@app.route('/')
def root():
    return redirect('/iss')

# ISS route
@app.route('/iss')
def iss():
    return render_template('home_page.html')

# Sign up
@app.route('/signup', methods=["GET", "POST"])
def signup():
    
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
        
    form = SignUpForm()
    
    if form.validate_on_submit():
        try:
            user = User.signup(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=form.password.data
            )
            db.session.commit()
            
        except IntegrityError as e:
            return render_template('auth/signup.html', form=form)
            
        do_login(user)
        return redirect('/')
    else:
        return render_template('auth/signup.html', form=form)
 
 # Login
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
@app.route('/logout')
def logout():
    do_logout()
    return redirect('/')














