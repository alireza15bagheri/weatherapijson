import requests

def weatherCondition(user_api_key):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    city_name = input('Enter city name: ')
    return base_url + city_name + '&appid=' + user_api_key

api_key = 'bea5d060970c6e59823b8c98b41c7d49'

url = weatherCondition(user_api_key = api_key) # get the data with the specific API_KEY provided by the website
data = requests.get(url).json()

if data['cod'] == '404':
    print(data['message'])
else:
    data_specs = data['main']

    t = data_specs['temp']
    tc = t - 273.15 # kelvin to C
    print('temperature: ' + str(round(tc,2)) + 'c')

    p = data_specs['pressure']
    print('pressure: ' + str(p) + 'hpa')

    h = data_specs['humidity']
    print('humidity: ' + str(h) + '%')

    desc = data['weather']
    desc = desc[0]['description']
    print(desc)