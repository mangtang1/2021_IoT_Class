
import RPi.GPIO as GPIO
import time

# GPIO 7개 핀 번호 설정

SEGMENT_PINS = [2,3,4,5,6,7,8]
DIGIT_PINS = [10,11,12,13]

GPIO.setmode(GPIO.BCM)

for i in SEGMENT_PINS:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,GPIO.LOW)

# Digit핀은 HIGH->OFF, LOW->ON LOW 여야지 거기에 출력을 한다는거임
for i in DIGIT_PINS:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,GPIO.HIGH)
# Common Cathode (HIGH->ON, LOW->OFF)

pict = [[1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0],
        [1,1,0,1,1,0,1],
        [1,1,1,1,0,0,1],
        [0,1,1,0,0,1,1],
        [1,0,1,1,0,1,1],
        [1,0,1,1,1,1,1],
        [1,1,1,0,0,1,0],
        [1,1,1,1,1,1,1],
        [1,1,1,0,0,1,1]]

def display(digit, number):

    for i in range(len(DIGIT_PINS)):
        if i + 1 == digit:
            GPIO.output(DIGIT_PINS[i],GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i],GPIO.HIGH)

        for i in range(len(SEGMENT_PINS)):
            GPIO.output(SEGMENT_PINS[i],data[number][i])

        time.sleep(0.001) # 1ms

try:
    
    while True:
        display(1,2)
        display(2,0)
        display(3,2)
        display(4,1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')