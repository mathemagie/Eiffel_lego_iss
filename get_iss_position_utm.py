import time
import requests
import json
from  LatLongUTMconversion import * 

file = "lights.txt"

def get_iss_position():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    obj = json.loads(response.content)
    return obj['iss_position']['latitude'], obj['iss_position']['longitude']


def swicth_on():
    f = open(file, "w")
    f.write("1")
    f.close()

def swicth_off():
    f = open(file, "w")
    f.write("0")
    f.close()

while 1:
    lat, lng = get_iss_position()
    lat = float(lat)
    lng = float(lng)
    print ("ISS lat : " + str(lat), ", lng : " + str(lng))
    (z, e, n) = LLtoUTM(23,lat, lng)
    print ("UTM : " + z)
    if z == '30T' or z == '31T' or z == '31U' or z == '30U': 
        swicth_on()
    else:
        swicth_off()
    time.sleep(2)
