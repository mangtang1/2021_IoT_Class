import RPi.GPIO as GPIO

LED_PIN = [4,17,27]
print(GPIO.BCM,LED_PIN,GPIO.IN,GPIO.OUT,GPIO.HIGH,GPIO.LOW)
GPIO.setmode(GPIO.BCM)
for i in range(len(LED_PIN)):
    GPIO.setup(LED_PIN[i],GPIO.OUT)

try:

    while True:
        
        x = int(input())
        if x==-1:
            break
        y = int(input())
        GPIO.output(LED_PIN[x],y)

finally:
    GPIO.cleanup()    
    print("cleanup and exit")
