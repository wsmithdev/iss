from twilio_ import send_email, send_text
from models import User

# Send notification
def send_notification(user_id, timeUntilPass):
    user = User.query.get(user_id)
    
    message = f'Hi {user.first_name}, the ISS will be visable from your location in {timeUntilPass}!'
    print(message)
    # Send text
    if user.notification_method_id == 1:
        send_text(message, user.cellphone)
        
    # Send email
    if user.notification_method_id == 2:
        send_email(message, user.email)