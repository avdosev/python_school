import requests as req

cityID = 472757 # Volgograd
apikey = "074390fbe455e62f1e92d57331c0fcf7"
lang = "ru"

api_url = {
    'current_day': 'http://api.openweathermap.org/data/2.5/weather',
    'next_hours': 'http://api.openweathermap.org/data/2.5/forecast'
}

res = req.get(api_url['next_hours'], params={
    'id': cityID,
    'units': 'metric',
    'APPID': apikey,
    'lang': lang
})

json_data = res.json()

print(json_data)