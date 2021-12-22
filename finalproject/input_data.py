import json
import random
#[17, 36, 22, 15, 8, 2]
F_gender = "F"
M_gender = "M"
phone="01012345678"
time = (1,2,3,4,5,6)

def rand_age(age):
    return random.randrange(age,age+10)

def rand_name(leng):
    res = ""
    for i in range(leng):
        res+=chr(random.randrange(ord('a'),ord('z')))
    return res

def rand_phone():
    return "010%08d"%random.randrange(0,100000000)

def rand_date():
    return (2021, random.randrange(1,13), random.randrange(1,29), random.randrange(0,24), random.randrange(0,60), random.randrange(0,60))

def ins(name,gender,age,phone,grade,time):
    with open('datas.json','r') as f:
        store_datas=json.load(f)
    user_info = {}
    user_info["name"]=name
    user_info["gender"]=gender
    user_info["age"]=age  #랜덤으로 정하기
    user_info["phone"]=phone
    user_info["grade"]=grade
    user_info["time"]="%04d/%02d/%02d %02d:%02d:%02d"%time
    store_datas["total_grade"]=store_datas["total_grade"]+grade
    store_datas["review_count"]=store_datas["review_count"]+1
    store_datas["datas"].append(user_info)
    with open('datas.json','w',encoding='utf-8') as make_file: # 새 정보 갱신
        json.dump(store_datas,make_file,indent='\t')

for i in range(51):
    age = rand_age(10)
    name=rand_name(10)
    phone=rand_phone()
    time=rand_date()
    grade = random.randrange(40,100)
    ins(name,M_gender,age,phone,grade,time)

for i in range(119):
    age = rand_age(10)
    name=rand_name(10)
    phone=rand_phone()
    time=rand_date()
    grade = random.randrange(70,100)
    ins(name,F_gender,age,phone,grade,time)

for i in range(144):
    age = rand_age(20)
    name=rand_name(10)
    phone=rand_phone()
    time=rand_date()
    grade = random.randrange(40,70)
    ins(name,M_gender,age,phone,grade,time)

for i in range(216):
    age = rand_age(20)
    name=rand_name(10)
    phone=rand_phone()
    time=rand_date()
    grade = random.randrange(50,73)
    ins(name,F_gender,age,phone,grade,time)

for i in range(110):
    age = rand_age(30)
    name=rand_name(10)
    phone=rand_phone()
    time=rand_date()
    grade = random.randrange(20,60)
    ins(name,M_gender,age,phone,grade,time)

for i in range(110):
    age = rand_age(30)
    name=rand_name(10)
    phone=rand_phone()
    time=rand_date()
    grade = random.randrange(40,80)
    ins(name,F_gender,age,phone,grade,time)

for i in range(60):
    age = rand_age(40)
    name=rand_name(10)
    phone=rand_phone()
    time=rand_date()
    grade = random.randrange(40,70)
    ins(name,M_gender,age,phone,grade,time)

for i in range(90):
    age = rand_age(40)
    name=rand_name(10)
    phone=rand_phone()
    time=rand_date()
    grade = random.randrange(25,75)
    ins(name,F_gender,age,phone,grade,time)

for i in range(16):
    age = rand_age(50)
    name=rand_name(10)
    phone=rand_phone()
    time=rand_date()
    grade = random.randrange(10,50)
    ins(name,M_gender,age,phone,grade,time)

for i in range(64):
    age = rand_age(50)
    name=rand_name(10)
    phone=rand_phone()
    time=rand_date()
    grade = random.randrange(20,60)
    ins(name,F_gender,age,phone,grade,time)

for i in range(4):
    age = rand_age(60)
    name=rand_name(10)
    phone=rand_phone()
    time=rand_date()
    grade = random.randrange(10,40)
    ins(name,M_gender,age,phone,grade,time)

for i in range(16):
    age = rand_age(60)
    name=rand_name(10)
    phone=rand_phone()
    time=rand_date()
    grade = random.randrange(25,75)
    ins(name,F_gender,age,phone,grade,time)
