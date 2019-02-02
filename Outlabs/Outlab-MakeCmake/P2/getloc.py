# ! python3

import requests
import datetime


def iss_location():
    issLink = 'http://api.open-notify.org/iss-now.json'
    res = requests.get(issLink)
    dictLoc = res.json()
    latitude = dictLoc["iss_position"]["latitude"]
    longitude = dictLoc["iss_position"]["longitude"]
    print('Current Location of ISS')
    print('Latitude : ' + str(latitude))
    print('Longitude : ' + str(longitude))


def pass_time():
    print('Enter Details to know when ISS will pass over a location:')
    latitude = input('Latitude :')
    longitude = input('Longitude :')
    link = 'http://api.open-notify.org/iss-pass.json'
    payload = {'lat': latitude, 'lon': longitude}
    #?lat='+str(latitude)+'&lon='+str(longitude)
    res = requests.get(link, params=payload)
    dictLoc = res.json()
    risetime = dictLoc["response"][0]["risetime"]
    duration = dictLoc["response"][0]["duration"]
    durMin = int(duration / 60)
    durSec = duration % 60
    timeNow = datetime.datetime.fromtimestamp(risetime)
    day = timeNow.day
    month = timeNow.month
    year = timeNow.year
    hour = timeNow.hour
    minute = timeNow.minute
    print('Date : ' + str('{:02}'.format(day)) + '/' + str('{:02}'.format(month)) + '/' + str(year))
    print('Time : ' + str('{:02}'.format(hour)) + ':' + str('{:02}'.format(minute)))
    print('For : ' + str(durMin) + ' minutes and ' + str(durSec) + ' seconds')


def people_info():
    link = 'http://api.open-notify.org/astros.json'
    res = requests.get(link)
    dictAstros = res.json()
    listAstros = dictAstros["people"]
    print('People currently in space: ' + str(len(listAstros)))
    i = 1
    for astro in listAstros:
        print(str(i) + '. ' + astro["name"])
        i = i + 1


if __name__ == "__main__":
    iss_location()
    pass_time()
    people_info()
