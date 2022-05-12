from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

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

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    location_id = db.Column(db.Integer, nullable=True)
    notification_method_id = db.Column(db.Integer, nullable=True)
    
    # Sign up 
    @classmethod
    def signup(cls, first_name, last_name, email, password):
        
        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode('UTF-8')
        
        # Create user
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_password
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