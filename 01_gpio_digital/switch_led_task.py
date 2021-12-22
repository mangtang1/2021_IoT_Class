import RPi.GPIO as GPIO

count = 3
switch_pin = [21,16,20]
led_pin = [22,17,27]

GPIO.setmode(GPIO.BCM)

for i in range(count):
    GPIO.setup(led_pin[i],GPIO.OUT)
    GPIO.setup(switch_pin[i],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        for i in range(count):
            val = GPIO.input(switch_pin[i])
            GPIO.output(led_pin[i],val)
            
finally:
    GPIO.cleanup()
    print('clean up and exit')