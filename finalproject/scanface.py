
# relative_path = '/home/pi/src5/finalproject/'
relative_path = ''

from tensorflow.keras.preprocessing.image import img_to_array
import imutils
import cv2
from tensorflow.keras.models import load_model
import numpy as np

# 학습된 모델 경로를 불러옴


detection_model_path = relative_path + 'Emotion-recognition-master/haarcascade_files/haarcascade_frontalface_default.xml'
emotion_model_path = relative_path + 'Emotion-recognition-master/models/_mini_XCEPTION.102-0.66.hdf5'

# 얼굴 인식과 감정인식 모델을 불러옴
face_detection = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
emotion_classifier = load_model(emotion_model_path, compile=False)
EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised", "neutral"]

# 감정인식 함수
def measure_feeling(picture):
    
    frame = picture
    #사진을 적당한 크기로 리사이즈 해줌
    frame = imutils.resize(frame,width=300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
    
    canvas = np.zeros((250, 300, 3), dtype="uint8")
    frameClone = frame.copy()
    if len(faces) > 0:
        faces = sorted(faces, reverse=True,        
        key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
        (fX, fY, fW, fH) = faces
                    # 얼굴 사진을 추출한뒤 28*28 픽셀로 만들고 ROI를 CNN(추출한 자료에서 직접 학습 후 처리하는 방식)을 통하여 분석한다 
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (64, 64))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
                
        preds = emotion_classifier.predict(roi)[0]
        emotion_probability = np.max(preds)
        label = EMOTIONS[preds.argmax()]
    
        score = 0 #감정 점수
        #감정의 종류에 따라서 점수를 계산함
        for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
            if i==0 or i==1 or i==2 or i==4 : 
                score = score - prob 
            elif i==3 or i==5 :
                score = score + prob
            elif i==6:  
                score = score
            
        return ((score+1)*50, preds)
    else:
        return ('not_detected',[])