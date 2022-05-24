import urllib.request, json

# Get ISS current location
def get_ISS_location():
    URL = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(URL)
    data = response.read()
    iss_location = json.loads(data)
    return iss_location
    