from models import db, Notification
from app import app

# Create tables
db.drop_all()
db.create_all()

# Seed data
email = Notification('Email')
text = Notification('Text')
none = Notification('None')

db.session.add(email)
db.session.add(text)
db.session.add(none)