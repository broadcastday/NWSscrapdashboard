import json
import requests
url ="https://api.weather.gov/gridpoints/LOX/150,52/forecast"
headers = {
    'User-Agent': '(Python 3.11, Student)',
    'Accept': 'application/ld+json'

}

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)




reqload = requests.get(url,headers=headers)
response = json.loads(reqload.text)
#jprint(response.json())

jsonget = reqload.json()

#dewpoints = jsonget['periods']['dewpoint']["value"]["number"]
for number in jsonget:
    if (jsonget['number']) < 4:
        print(jsonget['periods']['dewpoint']['value'])
