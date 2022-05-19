import os
import time
import urllib.request, json
from models import User, Location
from notify import send_notification
from helpers import to_mm_ss



def iss_passes(lat, long):
    URL = f'https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/{lat}/{long}/0/10/300/&apiKey={os.environ.get("N2YO_API_KEY")}'
    response = urllib.request.urlopen(URL)
    data = response.read()
    iss_passes = json.loads(data)
    return iss_passes

def get_next_pass():
    users = User.get_all_for_notifications()
    for user in users:
        # Get visable passes
        location = Location.query.get(user.id)
        passes = iss_passes(location.lat, location.long)
        
        # How long before the next visable pass
        timeUntilPass = passes["passes"][0]["maxUTC"] - int(time.time())
        
        # Send notification
        if timeUntilPass < 3600:
            send_notification(user, to_mm_ss(timeUntilPass))

         