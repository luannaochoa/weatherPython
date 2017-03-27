import pyowm 

owm = pyowm.OWM('0dbae436ba2e6db34a91887441471ed3')
observation = owm.weather_at_place("Miami, US")
w = observation.get_weather()
wind = w.get_wind()
temperature = w.get_temperature('fahrenheit')
tomorrow = pyowm.timeutils.tomorrow()
print(temperature['temp_max'])
#print(w)
#print(wind)
print(temperature)
#print(tomorrow)
