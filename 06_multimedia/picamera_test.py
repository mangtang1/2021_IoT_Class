import picamera
import time

path = "/home/pi/src/06_multimedia"
camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.start_preview()

try:
    while 1:
        x = int(input("photo:1, video:2, exit:9 > "))
        now_str = time.strftime("%Y%m%d_%H%M%S")
        if x == 1:
            time.sleep(3)
            camera.rotation = 0
            camera.capture('%s/photo_%s.jpg' % (path,now_str))             #사진 촬영
            print("사진 촬영")
            
        elif x == 2:
            camera.rotation = 0
            camera.start_recording('%s/video_%s.h264' % (path,now_str))
            x = input("press enter to stop recording")
            camera.stop_recording()
            print("동영상 촬영")

        elif x == 9:
            break

        else :
            print("incorrect command")

finally:
    camera.stop_preview()
    exit(0)