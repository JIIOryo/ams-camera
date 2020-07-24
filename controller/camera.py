import sys

import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from service.camera import take_picture
from service.trimming import trimming
from service.uploader import s3_upload

tmp_picture_path = '/home/pi/ams-camera/tmp/now.jpg'

def picture(request: dict) -> None:

    take_picture(
        file_ = tmp_picture_path,
        x = request['resolution']['x'],
        y = request['resolution']['y'],
        warm_up_time = request['cameraWarmUpTime']
    )

    trimming(
        file_ = tmp_picture_path,
        top = request['trimming']['top'],
        bottom = request['trimming']['bottom'],
        left = request['trimming']['left'],
        right = request['trimming']['right']
    )

    s3_upload(
        file_ = tmp_picture_path,
        object_name = request['objectName'],
        access_key_id = request['uploader']['aws']['accessKeyId'],
        secret_access_key = request['uploader']['aws']['secretAccessKey'],
        bucket = request['uploader']['aws']['s3Bucket'],
        region = request['uploader']['aws']['region'],
    )
