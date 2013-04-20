#! /usr/bin/python
#Written By Tom Paulus, @tompaulus, www.tompaulus.com

from threading import Timer
from lib.Char_Plate.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import smbus
import time
from lib.Scroller import Scroller
import requests

version = 0
boardVersion = '/proc/cpuinfo'
API_KEY = '3fad5yeebnw6q27en4p2qsxm'


def init():
    global lcd
    if version == 0:
        lcd = Adafruit_CharLCDPlate(busnum=0)
        lcd.clear()
        lcd.backlight(lcd.ON)
    elif version == 1:
        lcd = Adafruit_CharLCDPlate(busnum=1)
        lcd.clear()
        lcd.backlight(lcd.ON)
    else:
        quit("Raspberry Pi Version Error!")

    lcd.clear()
    lcd.backlight(lcd.ON)
    lcd.message('News Client\nfor Raspberry Pi')
    time.sleep(1)
    lcd.clear()
    lcd.message('Version 1.0\nTom Paulus 2013')
    time.sleep(1)
    lcd.clear()


def rotate(s, number):
    print number
    lcd.clear()
    lcd.message('\n               ' + str(number))  # Print the Article Number in the bottom right corner
    lcd.home()
    lcd.message(s)


def get(count, key):
    """
    Get the homepage form USA Today
    :return: JSON object
    """
    url = 'http://api.usatoday.com/open/articles/topnews/news?count=' + str(count) + \
          '&days=0&page=0&encoding=json&api_key=' + key

    d = requests.get(url)                                                        # REST Get to USA TODAY API
    JSON = d.json()                                                              # Convert Get to JSON
    return JSON                                                                  # Return to main thread


tools = Scroller()
articles = list()
currentTitle = 0
z = 0
update = True

init()

while True:
    z = 0
    if update:
        #Create a list form the 9 newest articles from the USA Today
        nJson = get(9, API_KEY)
        length = len(nJson['stories'])
        for x in range(0, length):
            articles.append(nJson['stories'][x]['title'])
        update = False

    display = tools.splitString(articles[currentTitle], 15)  # Make the Headline fit our display
    for y in range(0, len(display)):
        z += 1
        Timer(y * 2, rotate, args=[display[y], currentTitle + 1]).start()  # Auto scroll through the headline
    time.sleep(z * 2 + 2)
    currentTitle = (currentTitle + 1) % len(articles)  # Move to the next article