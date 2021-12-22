from flask import Flask, Blueprint, request, render_template
import json
from collections import OrderedDict
from numpy.core.numeric import NaN
import requests
import time
from const_data import *

# relative_path = '/home/pi/src5/finalproject/'
from makestatics import make_stick, make_circle
bp_viewdata = Blueprint('view', __name__, url_prefix='/viewdatas')
chosen_store = "store1"

def update_chosen_store(**args):
    with open(relative_path+store_path,'r') as f:
        stores_datas=json.load(f)

    global chosen_store
    if args.get("chosen_store") != None:
        stores_datas["chosen_store"]=args.get("chosen_store")
        with open(relative_path+store_path,'w',encoding='utf-8') as make_file: # 새 정보 갱신
            json.dump(stores_datas,make_file,indent='\t')

    chosen_store = stores_datas.get("chosen_store")


def push_data_user(dict): # QR 코드 만들 때 받은 유저 데이터를 넣음
    with open(relative_path+user_path,'r') as f:
        user_datas=json.load(f)
    

    user_datas[dict.get("name")]=dict # 원래 거에다가 업데이트 해서 json을 고침
    with open(relative_path+user_path,'w',encoding='utf-8') as make_file:
        json.dump(user_datas,make_file,indent='\t')

def push_data_store(qr_data, feel_data, total_grade, review_count): # 유저들의 평가 정보를
    with open(relative_path+store_path,'r') as f:
        stores_datas=json.load(f)
    store_datas= stores_datas.get(chosen_store)

    cur_grade=store_datas.get("total_grade") # 새롭게 총점과 리뷰 개수를 갱신
    cur_count=store_datas.get("review_count")
    store_datas["total_grade"]=total_grade=cur_grade+feel_data["grade"]
    store_datas["review_count"]=review_count=cur_count+1

    user_info=json.loads(qr_data.replace("'",'"')) # json 형식에 맞게끔 따옴표를 고침
    user_info.update(feel_data)#목화솜 채집 마스터 김명우

    now=time.localtime() # 현재 시각 저장
    user_info["time"]="%04d/%02d/%02d %02d:%02d:%02d"%(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec)

    store_datas["datas"].append(user_info) # 새롭게 입력받은 유저 정보를 리스트에 추가함
    stores_datas[chosen_store]=store_datas

    with open(relative_path+store_path,'w',encoding='utf-8') as make_file: # 새 정보 갱신
        json.dump(stores_datas,make_file,indent='\t')

    return total_grade, review_count

def get_logs(): # 현재의 로그를 출력하기 위한 형태로 반환
    with open(relative_path+store_path,'r') as f:
        stores_datas=json.load(f)
    store_datas= stores_datas.get(chosen_store)

    global total_grade, review_count
    total_grade = store_datas.get("total_grade",0)
    review_count = store_datas.get("review_count",0)
    ave_score=0
    if review_count != 0:
        ave_score=total_grade/review_count

    return ave_score, store_datas.get("store_name"), total_grade, review_count

@bp_viewdata.route("/",methods=['GET','POST']) # 통계 출력
def view_user_data():

    if request.args.get("store") != None:
        val = request.args.get("store")
        if val.isdigit() : val = "store"+val
        update_chosen_store(chosen_store = val)

    with open(relative_path+store_path,'r') as f:
        stores_datas=json.load(f)
    store_datas= stores_datas.get(chosen_store)

    if len(store_datas.get("datas")) <= 0:
        return '''No Data<br><br>
        <a href = "/">돌아가기</a>
        '''

    best_age, worst_age = make_stick()
    make_circle()
    return render_template("viewdatas.html",store_name=store_datas.get("store_name"),view_stick="datas/stick_figure.png",view_circle="datas/circle_figure.png", best_age=best_age, worst_age=worst_age)