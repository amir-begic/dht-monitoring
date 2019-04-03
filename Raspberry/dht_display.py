import lcddriver
import time
import Adafruit_DHT
import RPi_I2C_driver
import requests
 
sensor = Adafruit_DHT.DHT11
pin = 4

temp = 0
humi = 0

#url = 'http://localhost:9201/99'
  
#lcd = lcddriver.lcd()
lcd = RPi_I2C_driver.lcd()

#lcd.lcd_display_string("RPi I2C test", 1)
lcd.lcd_clear()
 
while True:
    time.sleep(5)
    url = 'http://localhost:9201/99'
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print(humidity)
    print(temperature)
    if humidity is not None and temperature is not None:
            lcd.lcd_display_string('Temp.: {0:0.1f} C'.format(temperature), 1)
            lcd.lcd_display_string('Humidity: {0:0.1f} %'.format(humidity), 2)
            #post data to webservice: [:-3] , [:-2]
            temp = int(temperature)
            humi = int(humidity)
            url += '/' + str(temp) + '/' + str(humi)
            res = requests.get(url)
            #res = requests.post(url)
            print(res.text)
    else:
            print('Fehler beim Einlesen der Daten. Starte einen weiteren Versuch!')
  
time.sleep(5)