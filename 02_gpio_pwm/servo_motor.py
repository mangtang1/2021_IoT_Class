# servo_motor.py
import RPi.GPIO as GPIO

SERVO_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN,GPIO.OUT)

GPIO.PWM(SERVO_PIN,50)
pwm.start(7.5)

try:
    while True:
        input('1: -90, 2: 0, 3: +90, 0: exit>')
        if val == '1':
            pwm.ChangeDutyCyle(5) # -90도
        elif val == '2':
            pwm.ChangeDutyCycle(7.5) # 0도
        elif val == '3':
            pwm.ChangeDutyCycle(10) # 90도
        elif val == '9':
            break

finally:
    pwm.stop()
    GPIO.cleanup()

