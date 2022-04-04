#import urequests
#import ubinascii, uhashlib
import machine
#import json

import network

import ssd1306
import dht
from machine import Pin,I2C
from time import sleep
#import wifimgr



#dht pin setup
sensor = dht.DHT11(Pin(2))

#i2c
try:
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    addresses = i2c.scan()
    
    for address in addresses:
        print('address i2c',address)    
except:
    print("Could not find sensor")


oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)



#Set sleep time
deep_sleep_minutes = 5    #in minutes


while True:
#get humidity/temperature DHT22/11

    

    
    try:
        sensor.measure()
        dht_temp = sensor.temperature()
        dht_humidity = sensor.humidity()
    #if (isinstance(dht_temp, float)) or (isinstanc(dht_humidity, int) and isinstance(hum, int)):
    #    msg = (b'{0:3.1f},{1:3.1f}'.format(dht_temp, dht_humidity))
        print('temperature: %3.1f C' % dht_temp)
        print('humidity: %3.1f %%' % dht_humidity)
        hum_sensor_id = board_id + "ht1"
        temp_sensor_id = board_id + "temp"
    except Exception as e:
        print(e)
        print("Could not read DHT")
        status = 1

    try:
        temp = str(dht_temp)
        comma_position=temp.find('.')
        print(comma_position)
        comma_position = int(comma_position)+2
        temp = temp[:comma_position]
        print(temp)
        
        oled.fill(0)#clear oled
        sleep(3)
        oled.text('Room Temp:', 0, 0)
        oled.text(str(dht_temp), 85, 0)
        oled.text('C', 105, 0)
        
        oled.text('Humidity:', 0, 10)
        oled.text(str(dht_humidity), 85, 10)
        oled.text('%', 105, 10)

        oled.show()    #display data
    except Exception as e:
        print(e)
        print("Could not print on screen")


    print('i will sleep now for: 5 minutes and try again after that')
    #deep_sleep(deep_sleep_minutes*60)
    sleep(10)



