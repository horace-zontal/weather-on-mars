import urllib2
import json

f = urllib2.urlopen('http://marsweather.ingenology.com/v1/latest/.json')

json_string = f.read()

parsed_json = json.loads(json_string)

terra_date = parsed_json['report']['terrestrial_date']

min_temp = parsed_json['report']['min_temp']

max_temp = parsed_json['report']['max_temp']

pressure = parsed_json['report']['pressure']

pressure_trend = parsed_json['report']['pressure_string']

wind_speed = parsed_json['report']['wind_speed']

wind_direction = parsed_json['report']['wind_direction']

atmo_opacity = parsed_json['report']['atmo_opacity']

print "Terrestial Date: %s, Max Temp: %s, Min temp is: %s, Pressure: %s, Pressure Trend: %s, Wind Speed: %s, Wind Direction: %s, Atomospheric Opacity: %s" % (terra_date, min_temp, max_temp, pressure, pressure_trend, wind_speed, wind_direction, atmo_opacity)

f.close()