# International Space Station Tracker

[Check it out the live site!](https://sb-iss-tracker.herokuapp.com/)

*or*

Visit https://sb-iss-tracker.herokuapp.com

### What does it do?

This web app was created for users who would like to sign up for alerts in the form of a text message or an email to get notifified when the ISS will 
be visable from their location. 

### How to do it

Simply go to the live site, create an account, fill out some information, select a notification method and sit back and relax. You'll receive a text or email when the ISS is closeby. Don't worry,
the text or email will give you the exact T-Minus!

## Under the hood

### APIs

The following APIs were used to create this application:

- Geoapify
This API will be used to convert a typed address into geographic coordinates that will be required for other APIs.
https://www.geoapify.com/geocoding-api

- N2YO
This API will be used to get all the current information on the Internation Space Station including date/time of the next visable pass.
https://www.n2yo.com/

- Twilio
This API will be used to notify the user via email or text of the next visable pass.
https://www.twilio.com/docs/usage/api

### Technologies User

The following technologies were used the create this application:

- HTML
- CSS
- Jinja
- Python
- Flask
- PostgreSQL
- SQLAlchemy
