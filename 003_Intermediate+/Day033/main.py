import requests
from datetime import datetime
#
response = requests.get(url="http://api.open-notify.org/iss-now.json#")

data = response.json()
latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']

current_position = (latitude, longitude)
#
# print(current_position)
LATITUDE = 49.2107718
LONGITUDE = -123.0735743
parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", parameters)
response.raise_for_status()

data = response.json()['results']
sunrise = data['sunrise'].split("T")[1].split(":")[0]
sunset = data['sunset'].split("T")[1].split(":")[0]

print(sunrise)
# print(sunset)

current_time = datetime.now().hour

print(current_time)
