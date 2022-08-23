import requests
import PySimpleGUI as sg

def weather_data(zipcode):

    postCode = zipcode
    apiKey = "e47162aa3104ea108326b75e05eb5833"
    geoApiUrl = "http://api.openweathermap.org/geo/1.0/zip"
    weatherApiUrl = "https://api.openweathermap.org/data/2.5/weather"

    r = requests.get(url=geoApiUrl, params=dict(zip=postCode, appid=apiKey))
    data = r.json()

    lat = data['lat']
    lon = data['lon']

    r = requests.get(url=weatherApiUrl, params=dict(lat=lat, lon=lon, appid=apiKey))
    data = r.json()
    stringForm = f"Weather: {data['weather'][0]['main']}, {data['weather'][0]['description']} \nTemperature: {data['main']['temp']-273.15:.2f} C"
    return stringForm
weather_data("570150,SG")

sg.theme('SystemDefaultForReal')

layout = [  [sg.Text('Get weather data by zipcode')],
            [sg.Text('Enter zipcode (e.g 123456,SG)'), sg.InputText()],
            [sg.Text('Weather data outputs here', key="-TEXT-")],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Get weather data', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    window['-TEXT-'].update(f"Weather at {values[0]} Today\n{weather_data(values[0])}")

window.close()

