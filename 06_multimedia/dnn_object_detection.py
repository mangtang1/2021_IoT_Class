import cv2
import numpy as np

# 모델파일 : http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel
# 구성파일 : https://github.com/BVLC/caffe/tree/master/models/bvlc_googlenet
# 클래스이름 파일 : https://github.com/opencv/opencv/blob/4.1.0/samples/data/dnn/classification/classes_ILSVRC2012.txt
#
model = './dnn/bvlc_googlenet.caffemodel'
config = './dnn/deploy.prototxt'
classFile = './dnn/classification_classes_ILSVRC2021.txt'

# Load network
net = cv2.dnn.readNet(model, config)

classNames = None
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

img = cv2.imread('cat.jpg')

# blob 이미지 생성
blob = cv2.dnn.blobFromImage(img, 1, (224, 224), (104, 117, 123))

# 얼굴 인식
net.setInput(blob)
prob = net.forward()

out = prob.flatten()
classId = np.argmax(out)
confidence = out[classId]

text = '%s (%4.2f%%)' % (classNames[classId], confidence * 100)
cv2.putText(img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
