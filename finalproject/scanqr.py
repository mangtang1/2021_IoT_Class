# -*- coding: utf-8 -*- 
import time
import zbar
import cv2
import json



def measure_qrcode(picture):
    ret = ""
    # Zbar 라이브러리로 QR코드를 인식하기위해서 opcnCV로 이미지를 그레이 스케일로 읽어옴
    img = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    qrcode_data = ""
 
    #Zbar는 다중 QR 검출도 가능
    #인식된 QR 데이터들을 가져옴
    scanner = zbar.Scanner()
    results = scanner.scan(img)
    for result in results:
        qrcode_data = result.data
 
        if qrcode_data.decode("utf-8") != None:
            # QR 코드가 인식이 되었다면
            # 인식된 QR 코드의 데이터를 출력해준다
            return qrcode_data.decode("utf-8")

    
    # QR 코드가 인식이 되지 않았다면
    # QR Code not detected
    return "not_detected"