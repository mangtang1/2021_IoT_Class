
import RPi.GPIO as GPIO
import time

# GPIO 7개 핀 번호 설정

SEGMENT_PINS = [2,3,4,5,6,7,8]

GPIO.setmode(GPIO.BCM)

for i in SEGMENT_PINS:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,GPIO.LOW)

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

try:
    for num in range(10):
        for i in range(len(SEGMENT_PINS)):
            GPIO.output(SEGMENT_PINS[i],pict[num][i])

        time.sleep(1)

        
finally:
    GPIO.cleanup()
    print('bye')