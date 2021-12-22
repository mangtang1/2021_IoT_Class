import RPi.GPIO as GPIO
import time

LED_PIN_RED = 17
LED_PIN_YEL = 22
LED_PIN_GRE = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_RED,GPIO.OUT)
GPIO.setup(LED_PIN_YEL,GPIO.OUT)
GPIO.setup(LED_PIN_GRE,GPIO.OUT)

for i in range(5):
    GPIO.output(LED_PIN_GRE,GPIO.LOW)
    GPIO.output(LED_PIN_RED,GPIO.HIGH)
    time.sleep(2)
    
    GPIO.output(LED_PIN_RED,GPIO.LOW)
    GPIO.output(LED_PIN_YEL,GPIO.HIGH)
    time.sleep(2)
    
    GPIO.output(LED_PIN_YEL,GPIO.LOW)
    GPIO.output(LED_PIN_GRE,GPIO.HIGH)
    time.sleep(2)

GPIO.cleanup()
