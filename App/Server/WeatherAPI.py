# This python file/scripts is used to fetch weatherData (from openweathermap rest api) using User input in the Prediction Form...
# After getting the weather data , Here We predict the outpot power and pass the useful info into app.py file for displaying the result in html page...

import requests
from .Predict import predict
import os
import datetime



if "CLOUDANT_URL" in os.environ:
    API_KEY = os.environ['WEATHER_API_KEY']
    CITY = os.environ['CITY']
else:
    # This is a dummy API-KEY that may not work ... Please make sure to put a valid API-KEY ...
    API_KEY = '92c81ed746339dbd635e68fc7150cc8e'
    CITY = 'turkey'



def get_theoreticalPower(wind_speed,redius,efficiency):
   '''Theoretical Power = π/2 * r² * v³ * ρ * η
   π/2 = 1.570795
   r = redious
   v = wind_speed
   ρ = density_of_air = 1.2
   η = effciency
   '''
   theoreticalPower = [(lambda x: 1.570795*redius*redius*wind_speed[x]*wind_speed[x]*wind_speed[x]*1.2*efficiency)(x) for x in range(len(wind_speed))]
   return theoreticalPower



def get_all_Result(redius,efficiency,hours):
    api_url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid={}'.format(CITY,API_KEY)
    data = requests.get(api_url).json()

    if data['cod'] == "200":
        wind_deg = []
        date_time = []
        wind_speed = []
        humidity = []
        start = 0
        while True:     
            test_time = data['list'][start]['dt_txt']
            test_time = datetime.datetime.strptime(test_time,'%Y-%m-%d %H:%M:%S')
            if test_time > datetime.datetime.now():
                break
            else:
                start =  start + 1
        end = start + hours
        for i in range(start,end):
            wind_deg.append(data['list'][i]['wind']['deg'])
            humidity.append(data['list'][i]['main']['humidity'])
            date_time.append(data['list'][i]['dt_txt'])
            wind_speed.append(data['list'][i]['wind']['speed'])

        theoreticalPower = get_theoreticalPower(wind_speed,redius,efficiency)
        actualPower = predict(wind_speed,theoreticalPower)

        return actualPower,wind_speed,date_time,wind_deg,humidity

    else:
        return None
    