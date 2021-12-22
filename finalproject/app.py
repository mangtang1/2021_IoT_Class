
# relative_path = '/home/pi/src5/finalproject/'
relative_path = ''

from flask import Flask, render_template, Response, request
import cv2
import time
import numpy as np
import threading
from scanqr import measure_qrcode
import makeqrdata
import requests
import viewdata
import makestoredata
import json
from scanface import measure_feeling
from const_data import *

total_grade = 0
review_count = 0

CAMERA_WIDTH = 1000 # 기본 데이터 설정
CAMERA_HEIGHT = 800
NOT_FOUND = "not_detected"
Feeling_gage={"happiness":0,"anger":0,"sadness":0, "grade":0}
LOGS = "" 

qr_scanned=NOT_FOUND # 읽어드린 데이터들
face_scanned=NOT_FOUND

camera = cv2.VideoCapture(0) # 카메라와 blueprint 설정
app = Flask(__name__)
app.register_blueprint(makeqrdata.bp_makeqrdata)
app.register_blueprint(viewdata.bp_viewdata)
app.register_blueprint(makestoredata.bp_makestore)

# import RPi.GPIO as GPIO
# from control_oled import draw_OLED
# class RPB:
#     PIN_PIR_SENSOR = 17 # Pin 설정
#     PIN_BUTTON_CONFIRM = 5
#     PIN_PIEZO_BUZZER = 27
#     pwm = GPIO.PWM(PIN_PIEZO_BUZZER,262)

    

#     def __init__(self):
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(self.PIN_PIR_SENSOR, GPIO.IN)
#         GPIO.setup(self.PIN_BUTTON_CONFIRM, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#         GPIO.setup(self.PIN_PIEZO_BUZZER, GPIO.OUT)
#         self.pwm.start(0)

#     def get_PIR(self): # PIR 센서 감지
#         return GPIO.input(self.PIN_PIR_SENSOR) == GPIO.HIGH

#     def piezo_out(self, melody, accent, timelong): # PIEZO 관리
#         self.pwm.ChangeDutyCycle(accent)
#         self.pwm.ChangeFrequency(melody)
#         time.sleep(timelong)
#         self.pwm.ChangeDutyCycle(0)

#     def get_button_submit(self): # 서버 제출 버튼 확인
#         global qr_scanned, face_scanned, Feeling_gage, total_grade, review_count
#         while True:
#             if GPIO.input(self.PIN_BUTTON_CONFIRM)==GPIO.HIGH:
#                 while GPIO.input(self.PIN_BUTTON_CONFIRM)==GPIO.HIGH: pass
#                 print("inserted ")
#                 if qr_scanned != NOT_FOUND and face_scanned != NOT_FOUND:
#                     if self.get_PIR() == True:
#                         total_grade, review_count = viewdata.push_data_store(qr_scanned, Feeling_gage, total_grade, review_count)
#                         print("succeed")
#                         self.piezo_out(700,50,3)

#                     else:
#                         print("no PIR")
#                         self.piezo_out(400,50,3)
#                 else:
#                     self.piezo_out(200,50,3)

#             else:
#                 self.piezo_out(300,0,1)

#     def view_OLED(self): # OLED에 평점 출력
#         global total_grade, review_count
#         ave_score = 0
#         k=0
#         draw_OLED()
#         while True:
#             if review_count!=0:
#                 k=int(total_grade/review_count)

#             if ave_score != k :
#                 time.sleep(1)
#                 ave_score=k
#                 str="%d" %(ave_score)

#                 draw_OLED(text=str)

def gen_frames(): # 카메라 입력 받아서 인공지능으로 qr code와 표정 인식
    font = cv2.FONT_HERSHEY_COMPLEX
    font_size = 0.7
    font_thick = 1
    org=(30,700)
    while True:
        if camera.get(cv2.CAP_PROP_POS_FRAMES) == camera.get(cv2.CAP_PROP_FRAME_COUNT):
            camera.set(cv2.CAP_PROP_POS_FRAMES, 0)

        success, frame = camera.read()
        
        if not success:
            break
        else:
            current_picture = cv2.resize(frame, (CAMERA_WIDTH,CAMERA_HEIGHT)) #카메라를 입력받고 처리
            current_picture = cv2.rotate(current_picture, cv2.ROTATE_180) 
            global qr_scanned, face_scanned
            string_get=measure_qrcode(current_picture)
            if string_get != NOT_FOUND:
                qr_scanned=string_get

            global Feeling_gage #점수들 처리하기
            grade, feels= measure_feeling(current_picture)
            if grade != NOT_FOUND:
                Feeling_gage['anger']=int(feels[0]*100)
                Feeling_gage['sadness']=int(feels[4]*100)
                Feeling_gage['happiness']=int(feels[3]*100)
                Feeling_gage['surprising']=int(feels[5]*100)
                Feeling_gage['grade']=int(grade)    
                face_scanned="Happy : %d Sad : %d Angry : %d grade : %d"%(Feeling_gage['happiness'],Feeling_gage['sadness'],Feeling_gage['anger'],Feeling_gage['grade'])

                    
            ret, buffer = cv2.imencode('.jpg', current_picture) # 화면에 출력할 사진 jpg 로 만들기
            new_picture = buffer.tobytes()
            
            yield(b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + new_picture  + b'\r\n')

def make_status(): # 현재 읽어드린 데이터들을 이미지로 출력
    while True:
        global qr_scanned, face_scanned
        img = np.full(shape=(400,2048,3),fill_value=255,dtype=np.uint8)
        if qr_scanned != NOT_FOUND :
            qr_data=json.loads(qr_scanned)
            text=str(qr_data.get("name","No"))
        else :
            text=NOT_FOUND
        org=(50,100)
        font=cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, text, org, font, 2, (255,0,0),2)

        text=face_scanned
        org=(50,200)
        font=cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, text, org, font, 2, (255,0,0),2)

        ret, buffer = cv2.imencode('.jpg', img)
        new_picture = buffer.tobytes()
        yield(b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + new_picture  + b'\r\n')




@app.route('/',methods=['GET','POST']) # 메인 화면과 로그 받기
def mainpage():
    if(request.method!='GET'): # GET이 아니면 오류 띄우기
        return '''error'''
    
    if request.args.get("store") != None:
        val = request.args.get("store")
        if val.isdigit() : val = "store"+val
        viewdata.update_chosen_store(chosen_store = val)

    global total_grade, review_count
    ave_score, store_name, total_grade, review_count = viewdata.get_logs()
    return render_template('mainpage.html',ave_score=ave_score, store_name=store_name)

@app.route('/livecamera') # 카메라 화면 출력
def show_camera():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/showstatus') # 상태 화면 출력
def show_status():
    return Response(make_status(), mimetype='multipart/x-mixed-replace; boundary=frame')

if '__main__' == __name__: # flask 시작과 thread 돌리기
    try:
        # rpi = RPB() 
        # t1 = threading.Thread(target=rpi.get_button_submit,args=())
        # t1.start()
        # t2 = threading.Thread(target=rpi.view_OLED,args=())
        # t2.start()
        app.run(host='0.0.0.0', port=9000, debug=True)

    finally: # 마무리
        print("finish")
        camera.release()
        cv2.destroyAllWindows()
        # GPIO.cleanup()