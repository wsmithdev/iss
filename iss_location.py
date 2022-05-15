import urllib.request, json

# Get ISS current location
def get_ISS_location():
    URL = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(URL)
    data = response.read()
    iss_location = json.loads(data)
    print(iss_location)
    return iss_location
    