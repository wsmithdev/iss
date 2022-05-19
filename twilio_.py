import os
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
sendgrid_api_key = os.environ['SENDGRID_API_KEY']
sendgrid_from_email = os.environ['SENDGRID_FROM_EMAIL']

client = Client(account_sid, auth_token)

def send_text(text_message, cellphone_number):
    message = client.messages.create(
        body=text_message,
        from_="+19592072699",
        to=f'+1{cellphone_number}'
    )
    

def send_email(email_message, email):
    message = Mail(
    from_email=sendgrid_from_email,
    to_emails=email,
    subject='ISS will be visable soon!',
    html_content=f'<p>{email_message}</p>')
    sg = SendGridAPIClient(sendgrid_api_key)
    sg.send(message)
    