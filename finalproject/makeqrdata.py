from flask import Flask, Blueprint, request, render_template
import json
from collections import OrderedDict
import requests
import viewdata


# relative_path = '/home/pi/src5/finalproject/'
relative_path = ''

bp_makeqrdata = Blueprint('makeqr', __name__, url_prefix='/makeqr')

@bp_makeqrdata.route('/',methods=['GET','POST']) # GET 으로 입력받은 데이터로 QR 코드 만들기
def make_qrcode():
    if(request.method!='GET'): # GET이 아니면 오류 띄우기
        return '''error'''
    
    if request.args.get('name') != None: # 빈 공간이 아닌지 확인
        name=request.args.get('name')
        gender=request.args.get('gender')
        age=request.args.get('age')
        phone=request.args.get('phone')
        
        file_data={"name":name,"gender":gender,"age":age,"phone":phone} # data 생성

        # QR SERVER 에 보낼 데이터들 생성
        format={
            "frame_name":"bottom-frame",
            "qr_code_text": str(file_data),
            "image_format":"JPG",
            "frame_text":"Card",
            "frame_color":"#00D8FF",
            "frame_icon_name": "vcard",
            "frame_text":"Scan me",
            "foreground_color":"#000000",
            "background_color":"#FFFFFF"
        } 

        # QR 만드는 SERVER의 URL 
        url="https://api.qr-code-generator.com/v1/create?access-token=9c9VhgK7phmtyRw5OSopPnJ5iOUI3W80baFX7DEI1xjIvKxHQvTH-E5CsYDngdAh"
        
        # SERVER 의 데이터 전송 후 값 받기
        res = requests.post(url=url,data=format)
        
        # 저장할 파일의 위치와 이름 선정
        img_path = relative_path+"static/datas/qr_%s.jpg" % name

        # 파일에 받아온 이미지를 저장하고, QR CODE 를 화면에 띄움
        photo = open(img_path, "wb")
        photo.write(res.content)
        photo.close()
        viewdata.push_data_user(file_data)
        return render_template("makeqr.html",image_file="datas/qr_%s.jpg"%name)

    # 받아온 데이터가 없을시 그냥 양식만 띄움
    return render_template("makeqr.html")
    


