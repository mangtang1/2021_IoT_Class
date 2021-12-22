# 스위치로 LED 제어하기

import RPi.GPIO as GPIO

LED_PIN = 4
SWITCH_PIN = 12

GPIO.setmode(GPIO.BCM)

# LED를 출력모드로 설정
GPIO.setup(LED_PIN,GPIO.OUT)

# 안 누르면 LOW, 누르면 HIGH
GPIO.setup(SWITCH_PIN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        GPIO.output(LED_PIN,val)

finally:
    GPIO.cleanup()
    print('cleanup and exit')

