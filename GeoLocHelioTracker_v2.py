import math
import datetime
from datetime import date
import requests
from geopy.geocoders import Nominatim
from tkinter import *


master = Tk()
Label(master, text="Device Location (i.e. Zip Code, Address, Country)").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
Button(master, text='Enter Data', command=master.quit).grid(row=4, column=1, sticky=W, pady=4)
mainloop( )


# Use the input data to calculate the current position of the sun relative to device position
myLoc = e1.get()
print("Location: ",myLoc)

geolocator = Nominatim()
location = geolocator.geocode(myLoc)
print("Latitude & Longitude: ",(location.latitude, location.longitude))

lat = location.latitude
lon = location.longitude

now = datetime.datetime.now()

d0 = date(now.year, 1, 1)
d1 = date(now.year, now.month, now.day)
delta = d1 - d0

print("Current Time: ",now)

day_cntr = delta.days
time = now.hour+now.minute/60+now.second/3600

def SolarHour(h):   
	a = 15*(h-12)
	return a;

w = 15*(time-12)

def DeclineAng(t):   
	a = math.asin(0.39795*math.cos(0.98563*(t-173)*math.pi/180))/math.pi*180
	return a;

def SolarElevAng(d,l,w):   
	a = math.asin(math.sin(d*math.pi/180)*math.sin(l*math.pi/180)+math.cos(l*math.pi/180)*math.cos(w*math.pi/180)*math.cos(l*math.pi/180))/math.pi*180
	return a;

def SolarAzimAng(d,l,w,e):   
	a = math.acos((math.sin(d*math.pi/180)*math.cos(l*math.pi/180)-math.cos(d*math.pi/180)*math.cos(w*math.pi/180)*math.sin(l*math.pi/180))/math.cos(e*math.pi/180))/math.pi*180
	return a;

def SolarZenAng(e):   
	a = 90-e
	return a;

w=SolarHour(time)
decl=DeclineAng(day_cntr)
sol_elevation = SolarElevAng(decl,lat,w)
azimuth = SolarAzimAng(decl,lat,w,sol_elevation)

print("Solar Hour: ",'{:{width}.{prec}f}'.format(w, width=5, prec=3))
print("Solar Declination: ",'{:{width}.{prec}f}'.format(decl, width=5, prec=3))
print("Current Azimuth (deg): ",'{:{width}.{prec}f}'.format(azimuth, width=5, prec=3))
print("Current Solar Elevation (deg): ",'{:{width}.{prec}f}'.format(sol_elevation, width=5, prec=3))