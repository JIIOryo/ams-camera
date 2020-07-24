import time

import picamera

def take_picture(x: int, y: int, warm_up_time: int) -> None:
    with picamera.PiCamera() as camera:
        camera.resolution = (x, y)
        camera.start_preview()

        # warm up
        time.sleep(warm_up_time)

        camera.capture('/home/pi/ams-camera/tmp/now.jpg')
    return
