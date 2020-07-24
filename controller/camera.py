import sys

import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from service.camera import take_picture
from service.trimming import trimming

tmp_picture_path = '/home/pi/ams-camera/tmp/now.jpg'

def picture(request: dict) -> None:

    take_picture(
        file = tmp_picture_path,
        x = request['resolution']['x'],
        y = request['resolution']['y'],
        warm_up_time = request['cameraWarmUpTime']
    )

    trimming(
        file = tmp_picture_path,
        top = request['trimming']['top'],
        bottom = request['trimming']['bottom'],
        left = request['trimming']['left'],
        right = request['trimming']['right']
    )
