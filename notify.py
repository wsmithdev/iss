from twilio_ import send_email, send_text
from models import User
import os

# Send notification
def send_notification(user_id, timeUntilPass):
    enable = os.environ.get("ENABLE_NOTIFICATIONS")
    user = User.query.get(user_id)
    
    message = f'Hi {user.first_name}, the ISS will be visable from your location in {timeUntilPass}!'
    print(message)
    if enable == 'true':
        # Send text
        if user.notification_method_id == 1:
            send_text(message, user.cellphone)
            
        # Send email
        if user.notification_method_id == 2:
            send_email(message, user.email)