def kel_to_cel(temp: float):
    return round(temp-273.16)

def kel_to_far(temp: float):
    return round((kel_to_cel(temp) * (9/5)) + 32)

def unpack_weather_response(response: dict):
    new_weather_dict = {'Status' : response['weather'][0]['main'],
                'Description' : response['weather'][0]['description'],
                'Current Temperature' : f"{kel_to_cel(response['main']['temp'])} C ({kel_to_far(response['main']['temp'])} F)",
                'Feels Like' : f"{kel_to_cel(response['main']['feels_like'])} C ({kel_to_far(response['main']['feels_like'])} F)",
                'Min. Temperature' : f"{kel_to_cel(response['main']['temp_min'])} C ({kel_to_far(response['main']['temp_min'])} F)",
                'Max. Temperature' : f"{kel_to_cel(response['main']['temp_max'])} C ({kel_to_far(response['main']['temp_max'])} F)",
                'Pressure' : f"{response['main']['pressure']} hPa",
                'Humidity' : f"{response['main']['humidity']}%",
                'Wind Speed' : f"{response['wind']['speed']} m/s",
                'Direction' : f"{response['wind']['deg']} degree to North",
                'Location' : response['name']
            }
    return new_weather_dict