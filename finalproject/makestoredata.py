from flask import Flask, Blueprint, request, render_template
import json
from collections import OrderedDict
from numpy.core.numeric import NaN
import requests
import time
from const_data import *

# relative_path = '/home/pi/src5/finalproject/'
from makestatics import make_stick, make_circle
bp_makestore = Blueprint('mast', __name__, url_prefix='/makestore')

@bp_makestore.route('/',methods=['GET','POST']) # GET 으로 입력받은 데이터로 QR 코드 만들기
def make_store():
    if(request.method!='GET'): # GET이 아니면 오류 띄우기
        return '''error'''

    if request.args.get("name") != None:
        val = request.args.get("name")

        file_data={"store_name":val,"total_grade":0,"review_count":-1,"datas":[]} # data 생성

        with open(relative_path+store_path, "r") as f:
            stores_data = json.load(f)

        stores_data["store_count"]=stores_data["store_count"]+1

        stores_data["store%d"%(stores_data["store_count"])]=file_data

        
        with open(relative_path+store_path,'w',encoding='utf-8') as make_file: # 새 정보 갱신
            json.dump(stores_data,make_file,indent='\t')

    return render_template("makestore.html")



    