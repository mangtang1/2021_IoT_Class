import RPi.GPIO as GPIO # GPIO 선언
import time # time 선언

GPIO.setmode(GPIO.BCM) # BCM 모드로 설정

mel_acc = 50 # 피에조 부저 소리 크기

BUTTONS = [23, 24, 4, 26] # 1초, 10초, 1분, 리셋
PIEZO_PIN = 20 # 피에조 부저 핀
SEGMENT_PINS = [11, 19, 17, 15, 14, 5, 27] # 4 digits 핀 위치, ABCDEFG
DIGIT_PINS = [9, 6, 13, 22] # 자릿수 위치 1234
SERVO_PIN = 21 # 서보 모터 핀
timer_c = 0 # 타이머 설정 시간

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
        [1,1,1,0,0,1,1]] # 숫자들 저장

for i in SEGMENT_PINS: # 세그먼트 핀들 출력모드 설정

    GPIO.setup(i,GPIO.OUT)

for i in DIGIT_PINS: # 자릿수 핀들 출력모드 설정

    GPIO.setup(i,GPIO.OUT)

for i in BUTTONS: # 버튼 핀들 입력모드, pull_down 설정

    GPIO.setup(i,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(SERVO_PIN, GPIO.OUT) # 서보 모터 핀 출력모드 설정
servo = GPIO.PWM(SERVO_PIN,50) # 서보 모터 주파수 설정
servo.start(7.5) # 가운데로 시작

GPIO.setup(PIEZO_PIN,GPIO.OUT) # 피에조 핀 출력모드 설정
piezo = GPIO.PWM(PIEZO_PIN,1) # 피에조 객체 생성
piezo.start(mel_acc) # 시작

melody = [262,294,330,349,392,440,494,523] # 8음계 주파수 설정

def display(digit, number): # digit 자리에다가 number 출력

    for i in range(len(DIGIT_PINS)): # Digit_pins 개수만큼 반복
        if i + 1 == digit: # 만약 지금 i 가 출력하려는 digit 이면
            GPIO.output(DIGIT_PINS[i],GPIO.LOW) # 해당 digit을 low 로 설정을 해서 자리 지정
        else:
            GPIO.output(DIGIT_PINS[i],GPIO.HIGH) # 해당 digit을 high 로 설정을 해서 출력 안함 설정

    for i in range(len(SEGMENT_PINS)): # Segment_pins 개수만큼 반복
        GPIO.output(SEGMENT_PINS[i],num_pict[number][i]) # 해당 Segment 에다가 각 숫자의 데이터 값을 넣어서 출력

    time.sleep(0.001) # 0.001초 쉬기

    for i in range(len(DIGIT_PINS)): # 다 끄기
        
        GPIO.output(DIGIT_PINS[i],GPIO.HIGH)

    for i in range(len(SEGMENT_PINS)): # 다 끄기
    
        GPIO.output(SEGMENT_PINS[i],GPIO.LOW)


def disp4(inp, ti=30): # display에다가 각 자릿수를 구해서 보내서 출력함

    for i in range(ti): # 출력하는 시간인 ti 만큼 반복

        x=int(inp/1)%10 # 1의자리
        display(4,x) # 4번째에 출력
        x=int(inp/10)%10 # 10의자리
        display(3,x) # 3번째에 출력
        x=int(inp/100)%10 # 100의자리
        display(2,x) # 2번째에 출력
        x=int(inp/1000)%10 # 1000의 자리
        display(1,x) # 1번째에 출력
        time.sleep(0.001) # 0.001초로 쉬어서 잔상 남기기
    
def get_buttons(): # 현재 눌린 버튼들 파악

    res = [0,0,0,0,0] # 1s, 10s, 1m, reset, 여유 로 각 버튼의 눌림상태 확인
    for i in range(len(BUTTONS)): # 버튼 개수만큼 확인

        x=GPIO.input(BUTTONS[i]) # 버튼 입력값 받음
        res[i]=x # 그 값을 넣음

    return res # 버튼 입력 데이터 반환

def cont_subo(angle): # 서보 모터 조작

    val = angle/40.0 + 2.5 # 각도를 통한 모터 듀티싸이클 값 계산
    servo.ChangeDutyCycle(val) # 듀티 사이클 변환
    time.sleep(0.001) # 잠시 쉼

def cont_piezo(mel, acc): # 피에조 부저 조작, 멜로디, 세기

    piezo.ChangeFrequency(mel) # 멜로디로 주파수
    piezo.ChangeDutyCycle(acc) # 듀티싸이클로 세기
    
def time_end(): # 타이머 끝나면 일어나는 이벤트
    cont_piezo(300,mel_acc) # 피에조를 울림
    for i in range(4): # 네 번 이벤트 반복
        cont_subo(-90) # 서보 모터 -90도
        disp4(9999) # 9999 출력
        time.sleep(0.5) # 0.5 초 쉬었다가
        cont_subo(90) # 서보 모터 90도
        disp4(0000) # 0000 출력
        time.sleep(0.5) # 0.5 초 쉬었다가

    cont_piezo(10,0) # 피에조 소리 끄기
    time.sleep(1) # 1초 쉬기

def strat_timer(): # 사용자가 타이머를 시작함

    cont_subo(-90) # 서보 모터를 -90도로 옮기고
    cont_piezo(1,0) # 피에조 끔
    for i in range(timer_c,0,-1): # 시간을 사용자가 지정한 시간부터 1씩 깎아서 시간 표현, (1초가 컴퓨터의 성능에 따라 정확한 1초가 아닐 수 있음)
        disp4(i,300) # 시간을 300번 정도의 반복으로 출력
        cont_subo(i/timer_c*(180.0)-90) # 모터를 지금 시간에 비례하여서 움직이게 함
        bres = [0,0,0,0,0] # 버튼 입력을 받을 배열
        bres = get_buttons() # 버튼 입력 받음
        if bres[3] == 1: # 리셋이 눌렀다면
            break # 끝냄

    time_end() # 시간 끝냈을 때 이벤트 발생

try: # main 시작

    timer_c = 0 # 현재 시간 0 설정
    cont_piezo(1,0) # 피에조 소리 끄기
    while True: # 무한 반복

        bres = [0,0,0,0,0] # 버튼 입력 배열
        bres = get_buttons() # 버튼 입력 받음
        if bres[0]==1: # 1s 추가

            if bres[3]==1: # 리셋까지 같이 눌려있으면
                timer_c=0 # 지금시간 초기화

            else: # 1s 만 눌려있으면
                timer_c+=1 # 1초 추가
                cont_piezo(melody[3],mel_acc) # 파 소리 내기
                time.sleep(0.8) # 0.8초 쉬기

        elif bres[1]==1: # 10s 추가
            timer_c+=10 # 10초 추가
            cont_piezo(melody[4],mel_acc) # 솔 소리 내기
            time.sleep(0.8) # 0.8초 쉬기

        elif bres[2]==1: # 1m 추가
            timer_c+=60 # 1분 추가
            cont_piezo(melody[5],mel_acc) # 라 소리 내기
            time.sleep(0.8) # 0.8초 쉬기

        elif bres[3]==1: # 시작 reset 버튼
            cont_piezo(melody[6],mel_acc) # 시 소리 내기
            time.sleep(0.8) # 0.8초 쉬기
            strat_timer() # 타이머 시작

        time.sleep(0.005) # 0.005초 간격
        cont_piezo(1,0) # 피에조 부저 소리 끄기
        disp4(timer_c,30) # 현재 타이머 시간 출력
        
finally: # 비정상 멈춤

    GPIO.cleanup() # GPIO 초기화
    print("1528 전창우의 거북이 알람 타이머가 비정상적으로 끝났습니다 ㅠㅠ") # 에러 메세지
