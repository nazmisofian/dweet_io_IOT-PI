from sense_hat import SenseHat
import time
import requests
import os

sense = SenseHat()
sense.clear()

def sensors():
    temp_h = sense.get_temperature_from_humidity()
    temp_h = str(round(temp_h,1))
    humidity = sense.get_humidity()
    humidity = str(round(humidity, 2))
    url = 'https://dweet.io/dweet/for/DHT22Test?' + 'Temp=' + temp_h + '&Humidity=' + humidity
    r = requests.post(url)

    #viewForm change to formResponse, and add '&submit=Submit'
    #Change the link of the google form to the ones you have prepared
    #url_google = 'https://docs.google.com/forms/d/e/1FAIpQLScyxjg-mIGo98LJrU_GfzrXDF2AaJD0BPCgdFisXeuAImaMcg/formResponse?entry.462400853=' +temp_h+ '&entry.1250497753=' + humidity + '&sub$
    #g = requests.get(url_google)
    sense.show_message("T:" + str(temp_h) + "C", scroll_speed = 0.1)
    sense.show_message("H:" + str(humidity) + "%", scroll_speed = 0.1)

while True:
    sensors()
    time.sleep(10)
    print('Readings Recorded')
