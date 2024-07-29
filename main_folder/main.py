from typing import Optional
from fastapi import FastAPI, HTTPException, status
import requests, json
from .utils import unpack_weather_response
from .config import settings

app = FastAPI(title='Weather App', description="By entering the location's Coordinates or name of the City, you can access it's weather condition")

@app.get('/weather')
def get_location_weather(city: Optional[str] = None, lat: Optional[str] = None, lon: Optional[str] = None):
    if ((city is None) and (lat is None or lon is None)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid parameters provided.")
    elif ((city is not None) and (lat is not None or lon is not None)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Both Parameters provided. Enter Atmost one parameter")
    url = 'https://api.openweathermap.org/data/2.5/weather'
    response = None
    city_param = {'q' : city, 'appid' : settings.token}
    coord_param = {'lat' : lat, 'lon' : lon, 'appid' : settings.token}
    if city == None:
        response = requests.get(url=url, params=coord_param)
        response_dict = json.loads(response.text)
        return unpack_weather_response(response_dict)
    response = requests.get(url, city_param)
    response_dict = json.loads(response.text)
    return unpack_weather_response(response_dict)