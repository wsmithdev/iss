from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy import or_
from geoalchemy2.types import Geography

# Initialize Bcypt
bcrypt = Bcrypt()

# Connect to database
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
##############################################################################
# Models
##############################################################################    

########
# User
########
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    location_id = db.Column(db.Integer, nullable=True)
    notification_method_id = db.Column(db.Integer, nullable=True)
    cellphone = db.Column(db.Text, nullable=True)
    
    # Sign up 
    @classmethod
    def signup(cls, 
               first_name, last_name, email, password, 
               location_id,
               notification_method_id, cellphone
               ):
        
        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode('UTF-8')
        
        # Create user
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_password,
            location_id=location_id,
            notification_method_id=notification_method_id,
            cellphone=cellphone
        )
        
        # Add user to database
        db.session.add(user)
        
        return user
    
    # Authenticate user
    @classmethod
    def authenticate(cls, email, password):
        
        user = cls.query.filter_by(email=email).first()
        
        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            
            if is_auth:
                return user
            
        return False
    

    
###########
# Location
###########
class Location(db.Model):
    __tablename__ = 'location'
    
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Text, nullable=False)
    long = db.Column(db.Text, nullable=False)
    geolocation = db.Column(Geography('POINT'))
    
    # Add location to database
    @classmethod
    def add_location(cls, lat, long):
        
        #Create location model
        location = Location(
            lat=lat,
            long=long,
            geolocation=f'POINT({long} {lat})'
        )
        
        # Add to database
        db.session.add(location)
        
        return location
    
    # Get users within range, with notifications turned on
    @classmethod
    def get_users_in_range(cls, longitute, latitude, radius):
        users = db.session.execute(f'SELECT users.id, ST_Distance(ST_MakePoint({longitute}, {latitude}), location.geolocation) AS distance FROM users INNER JOIN location ON users.location_id = location.id WHERE ST_Distance(ST_MakePoint({longitute}, {latitude}), location.geolocation) < {radius} AND users.notification_method_id != 1;')
        return users
    
######################
# Notification Method
######################
class Notification(db.Model):
    __tablename__ = 'notification_method'
    
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.Text, nullable=False)

    
    # Add notification method to database
    @classmethod
    def add_notification_method(cls, method):
        
        #Create location model
        notification_method = Notification(
            method=method
        )
        
        # Add to database
        db.session.add(notification_method)
        
        return notification_method