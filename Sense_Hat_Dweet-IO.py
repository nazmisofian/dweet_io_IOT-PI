from sense_hat import SenseHat
import time
import requests

r = (255, 0, 0)
o = (255, 165, 0)
y = (255, 255, 0)
b = (30, 144, 255)
g = (0, 255, 0)
i = (75, 0, 130)
v = (238, 130, 238)
n = (135, 80, 22)
w = (255, 255, 255)
e = (0, 0, 0)

sense = SenseHat()
sense.clear()

def sensors():
    temp_h = sense.get_temperature_from_humidity()
    temp_h = str(round(temp_h,1))
    humidity = sense.get_humidity()
    humidity = str(round(humidity, 2))
    url = 'https://dweet.io/dweet/for/DHT22Test?' + 'Temp=' + temp_h + '&Humidity=' + humidity
    r = requests.post(url)

while True:
    sensors()
    time.sleep(10)
    print('Readings Recorded')
