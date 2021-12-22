import cv2

# 카메라로부터 VideoCapture 객체 생성
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 동영상 저장을 위한 VideoWriter 객체 생성
out = cv2.VideoWriter('output.avi',fourcc,30,(640,480))

while True:
    (ret, frame) = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    out.write(frame)

    if cv2.waitKey(10) == 27:
        break

# 사용자 지원 해제
cap.release()
out.release()
cv2.destroyAllWindows()