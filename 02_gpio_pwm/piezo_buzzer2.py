import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN,262) #주파수 소리의 높낮이
pwm.start(10) # 듀티 사이클 소리의 크기

melody = [262,294,330,349,392,440,494,523]

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)

finally:
    pwm.stop()
    GPIO.cleanup()