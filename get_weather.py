import requests

postCode = "521147,SG"
apiKey = "e47162aa3104ea108326b75e05eb5833"
geoApiUrl = "http://api.openweathermap.org/geo/1.0/zip"
weatherApiUrl = "https://api.openweathermap.org/data/2.5/weather"

r = requests.get(url=geoApiUrl, params=dict(zip=postCode, appid=apiKey))
data = r.json()

lat = data['lat']
lon = data['lon']

r = requests.get(url=weatherApiUrl, params=dict(lat=lat, lon=lon, appid=apiKey))
data = r.json()
print(data)

