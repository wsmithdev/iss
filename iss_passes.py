import urllib.request, json


def iss_passes(lat, long):
    URL = f'https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/{lat}/{long}/0/10/300/&apiKey=LYFLJY-PTWWYL-XKV96K-4HKF'
    response = urllib.request.urlopen(URL)
    data = response.read()
    iss_passes = json.loads(data)
    return iss_passes

