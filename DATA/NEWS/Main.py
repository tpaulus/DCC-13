#! /usr/bin/python
#Written By Tom Paulus, @tompaulus, www.tompaulus.com

from threading import Timer
from lib.Char_Plate.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import NewsAPI
import smbus
import time
from lib.Scroller import Scroller

version = 0
boardVersion = '/proc/cpuinfo'
API_KEY = '3fad5yeebnw6q27en4p2qsxm'

# try:
#     with open(boardVersion, 'r') as f:
#         for line in f:
#             version = (1 if line.rstrip()[-1] in ['1', '2'] else 2) - 1
# except IOError:
#     version = 0
#
# print version

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


def rotate(s):
    lcd.clear()
    lcd.message(s)


tools = Scroller()
API = NewsAPI.NewsAPI()
articles = list()
currentTitle = 0
z = 0
update = True

init()

while True:
    z = 0
    if update:
        nJson = API.get(15, API_KEY)
        length = len(nJson['stories'])
        for x in range(0, length):
            articles.append(nJson['stories'][x]['title'])
        update = False

    display = tools.splitString(articles[currentTitle], 16)
    for y in range(0, len(display)):
        z += 1
        Timer(y * 2, rotate, args=[display[y]]).start()
    time.sleep(z * 2 + 2)
    currentTitle = (currentTitle + 1) % len(articles)