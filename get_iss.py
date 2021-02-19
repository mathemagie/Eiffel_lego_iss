from skyfield.api import load, wgs84

from datetime import date
from datetime import datetime

from  LatLongUTMconversion import * 


today = date.today()

stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
satellites = load.tle_file(stations_url)
print('Loaded', len(satellites), 'satellites')

by_name = {sat.name: sat for sat in satellites}
satellite = by_name['ISS (ZARYA)']
#print(satellite)
print ("ISS (ZARYA) catalog #25544 \nepoch 2021-01-15 06:17:01 UTC")
#print(satellite.epoch.utc_jpl())

ts = load.timescale()
t = ts.now()

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print()
print("date and time =", dt_string)	

geocentric = satellite.at(t)
#print(geocentric.position.km)

subpoint = wgs84.subpoint(geocentric)

print (subpoint)
print('Latitude:', subpoint.latitude)
print('Longitude:', subpoint.longitude)
print('Elevation (m):', int(subpoint.elevation.m))
print ()

#(z, e, n) = LLtoUTM(23,subpoint.latitude, subpoint.longitude)

me = wgs84.latlon(48.873459,2.358040)

difference = satellite - me
#print(difference)

topocentric = difference.at(t)
#print(topocentric.position.km)

alt, az, distance = topocentric.altaz()

if alt.degrees > 0:
    print( 'The ISS is above the horizon')

#print (alt.degrees)
print("Altitude: ", alt)
print ("Azimut: ",az)
print ()
s = "The distance between my geographical \nposition and the ISS:"
print(s,int(distance.km), 'km')
