import sys

import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from service.camera import take_picture

def picture(request: dict) -> None:

    take_picture(
        x = request['resolution']['x'],
        y = request['resolution']['y'],
        warm_up_time = request['cameraWarmUpTime']
    )
