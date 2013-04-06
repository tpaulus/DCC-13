#! /usr/bin/python
#Written By Tom Paulus, @tompaulus, www.tompaulus.com
#For DCC 2013.1

import time

timeURL = 'http://json-time.appspot.com/time.json?tz='
zone = 'America/Phoenix'

while True:
    timeJson = requests.get(timeURL + zone).json()
    hour = timeJson['hour']
    minute = timeJson['minute']
    second = timeJson['second']
    dateTime = timeJson['datetime']
    print str(hour) + ':' + str(minute) + ':' + str(second)
    print dateTime
    time.sleep(1)