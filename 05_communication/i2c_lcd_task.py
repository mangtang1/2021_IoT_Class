from lcd import drivers
import time
import datetime
import Adafruit_DHT
import threading

display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
DHT_PIN = 4
datas=["","",""]
def get_current_DHT():
    while True:
        h, t = Adafruit_DHT.read_retry(sensor,DHT_PIN)
        datas[0]="%.1f*C, %2.1f%% "%(t,h)
        time.sleep(0.2)

def get_current_time():
    while True:
        now = datetime.datetime.now()
        datas[1]=now.strftime("%x%X")
        time.sleep(0.2)

def disp():
    display.lcd_display_string(datas[1], 1)
    display.lcd_display_string(datas[0], 2)

try:
    print("Writing to display")
    
    dht=threading.Thread(target=get_current_DHT,args=())
    tim=threading.Thread(target=get_current_time,args=())
    dht.start()
    tim.start()
    while True:
        disp()
        

finally:
    print("Cleaning Up")
    display.lcd_clear()
        