import cv2

# image 파일 읽기
img = cv2.imread('./ohmygirl.jpg')
img2 = cv2.resize(img, (300,200))

cv2.imshow('ohmygirl',img2)

# 키보드 입력을 기다림 (millisecond)
# 기본값 0, 0인 경우 키보드 입력이 있을 때까지 계속 기다림
cv2.waitKey(0)

# 열려있는 모든 창 닫기
cv.destroyAllWindows()