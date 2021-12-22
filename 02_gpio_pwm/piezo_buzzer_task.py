import RPi.GPIO as GPIO
import time

BUZZER_PIN = [17,27,22]
delay = 0.01
speed = 0.5
sud_acc = 40

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

pwm1 = GPIO.PWM(BUZZER_PIN[0],262) #주파수 소리의 높낮이
pwm2 = GPIO.PWM(BUZZER_PIN[1],262)
pwm3 = GPIO.PWM(BUZZER_PIN[2],262)
pwm1.start(sud_acc) # 듀티 사이클 소리의 크기
pwm2.start(sud_acc)
pwm3.start(sud_acc)
melody = [262,294,330,349,392,440,494,523]
sheet_high = [
[4,4,5,5,4,4,2,4,4,2,2,1,4,4,5,5,4,4,1,4,2,1,2,0],
[0,0,2,2,4,4,2,4,4,5,3,2,0,0,2,2,4,4,2,4,5,1,2,0,0],
[0,3,4,2,3,4,5,6,1,2,0,0,3,4,2,3,4,5,6,1,2,0,0,0]]
sheet_tempo = [1,1,1,1,1,1,2,1,1,1,1,3,1,1,1,1,1,1,2,1,1,1,1,3]

def sound(node,temp):

    pwm1.ChangeFrequency(melody[sheet_high[0][node]])
    pwm2.ChangeFrequency(melody[sheet_high[1][node]])
    pwm3.ChangeFrequency(melody[sheet_high[2][node]])
    pwm1.ChangeDutyCycle(sud_acc)
    pwm2.ChangeDutyCycle(sud_acc/2)
    pwm3.ChangeDutyCycle(sud_acc/3)

    time.sleep(temp*speed-delay)
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    pwm3.ChangeDutyCycle(0)
    
    time.sleep(delay)

try:
    for i in range(len(sheet_tempo)):
        sound(i,sheet_tempo[i])


finally:
    pwm1.stop()
    pwm2.stop()
    pwm3.stop()
    GPIO.cleanup()