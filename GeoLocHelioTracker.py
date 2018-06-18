import math
import datetime
from datetime import date
import requests
import json

send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']
print("Current Latitude: ",lat)
print("Current Longitude: ",lon)

now = datetime.datetime.now()

d0 = date(now.year, 1, 1)
d1 = date(now.year, now.month, now.day)
delta = d1 - d0

print("Current Time: ",now)

day_cntr = delta.days
time = now.hour+now.minute/60+now.second/3600

w = 15*(time-12)
declination = math.asin(0.39795*math.cos(0.98563*(day_cntr-173)*math.pi/180))/math.pi*180
sol_elevation = math.asin(math.sin(declination*math.pi/180)*math.sin(lat*math.pi/180)+math.cos(lat*math.pi/180)*math.cos(w*math.pi/180)*math.cos(lat*math.pi/180))/math.pi*180
azimuth = math.acos((math.sin(declination*math.pi/180)*math.cos(lat*math.pi/180)-math.cos(declination*math.pi/180)*math.cos(w*math.pi/180)*math.sin(lat*math.pi/180))/math.cos(sol_elevation*math.pi/180))/math.pi*180
zenith = 90-sol_elevation

print("Current Azimuth (deg): ",azimuth)
print("Current Solar Elevation (deg): ",sol_elevation)
