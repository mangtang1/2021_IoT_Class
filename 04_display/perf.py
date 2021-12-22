import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

mel_acc = 10

BUTTONS = [23, 24, 4, 26] # 1초, 10초, 1분, 리셋
PIEZO_PIN = 20
SEGMENT_PINS = [11, 19, 17, 15, 14, 5, 27]
DIGIT_PINS = [9, 6, 13, 22]
SERVO_PIN = 21
timer_c = 0

num_pict = [
        [1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0],
        [1,1,0,1,1,0,1],
        [1,1,1,1,0,0,1],
        [0,1,1,0,0,1,1],
        [1,0,1,1,0,1,1],
        [1,0,1,1,1,1,1],
        [1,1,1,0,0,0,0],
        [1,1,1,1,1,1,1],
        [1,1,1,0,0,1,1]]

for i in SEGMENT_PINS:

    GPIO.setup(i,GPIO.OUT)

for i in DIGIT_PINS:

    GPIO.setup(i,GPIO.OUT)

for i in BUTTONS:

    GPIO.setup(i,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(SERVO_PIN, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN,50)
servo.start(7.5)

GPIO.setup(PIEZO_PIN,GPIO.OUT)
piezo = GPIO.PWM(PIEZO_PIN,1)
piezo.start(mel_acc)

melody = [262,294,330,349,392,440,494,523]

def init(inp, mode):

    for i in inp:
        GPIO.setup(i,mode)

def display(digit, number):

    for i in range(len(DIGIT_PINS)):
        if i + 1 == digit:
            GPIO.output(DIGIT_PINS[i],GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i],GPIO.HIGH)

    for i in range(len(SEGMENT_PINS)):
        GPIO.output(SEGMENT_PINS[i],num_pict[number][i])

    time.sleep(0.001) # 1ms

    for i in range(len(DIGIT_PINS)):
        
        GPIO.output(DIGIT_PINS[i],GPIO.LOW)

    for i in range(len(SEGMENT_PINS)):
    
        GPIO.output(SEGMENT_PINS[i],GPIO.LOW)


def disp4(inp, ti=30):

    for i in range(ti):

        x=int(inp/1)%10
        display(4,x)
        x=int(inp/10)%10
        display(3,x)
        x=int(inp/100)%10
        display(2,x)
        x=int(inp/1000)%10
        display(1,x)
        time.sleep(0.001)
    
def get_buttons():

    res = [0,0,0,0,0]
    for i in range(len(BUTTONS)):

        x=GPIO.input(BUTTONS[i])
        res[i]=x

    return res

def cont_subo(angle):

    val = angle/20 + 10
    servo.ChangeDutyCycle(val)
    time.sleep(0.001)

def cont_piezo(mel, acc, delc=0.001):

    piezo.ChangeFrequency(mel)
    piezo.ChangeDutyCycle(acc)
    
def time_end():
    cont_piezo(300,mel_acc)
    for i in range(4):
        cont_subo(-90)
        disp4(9999)
        time.sleep(0.5)
        cont_subo(90)
        disp4(0000)
        time.sleep(0.5)

    cont_piezo(10,0)
    time.sleep(1)

def strat_timer():

    for i in range(timer_c,0,-1):
        disp4(i,300)
        cont_subo(int(i/timer_c*180)-90)

    time_end()

try:

    timer_c = 0
    while True:

        bres = [0,0,0,0,0]
        bres = get_buttons()
        if bres[0]==1:
            timer_c+=1
            cont_piezo(melody[3],10)

        elif bres[1]==1:
            timer_c+=10
            cont_piezo(melody[4],10)

        elif bres[2]==1:
            timer_c+=60
            cont_piezo(melody[5],10)

        elif bres[3]==1:
            cont_piezo(melody[6],10)
            strat_timer()

        time.sleep(0.005)
        disp4(timer_c,30)
finally:

    GPIO.cleanup()
    print("clean")
