from models import User, Location
from iss_passes import iss_passes
from flask import session
import time
import datetime

def continuous_call():
    while(True):
        get_next_pass()
        time.sleep(10)

def get_next_pass():
    users = User.get_all_for_notifications(1)
    for user in users:
        # Get visable passes
        location = Location.query.get(user.id)
        passes = iss_passes(location.lat, location.long)
        
        # How long before the next visable pass
        nextPassTime = passes["passes"][0]["maxUTC"] - int(time.time())
        
        # Send notification
        if nextPassTime < 999993600:
            print(f"A visable pass is happening in {nextPassTime} seconds for {user.first_name}!")
      
        
       
        
        
       
