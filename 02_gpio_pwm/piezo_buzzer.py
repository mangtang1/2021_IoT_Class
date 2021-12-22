import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN,262) #주파수 소리의 높낮이 조절
pwm.start(50) # 듀티 사이클, 소리의 크기 조절

time.sleep(2)
pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()