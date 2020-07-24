import sys

import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from service.camera import take_picture
from service.trimming import trimming
from service.uploader import s3_upload
from lib.config import get_config_item

TMP_PICTURE_PATH = get_config_item('tmp_picture_file_path')

def picture(request: dict) -> None:

    take_picture(
        file_ = TMP_PICTURE_PATH,
        x = request['resolution']['x'],
        y = request['resolution']['y'],
        warm_up_time = request['cameraWarmUpTime']
    )

    trimming(
        file_ = TMP_PICTURE_PATH,
        top = request['trimming']['top'],
        bottom = request['trimming']['bottom'],
        left = request['trimming']['left'],
        right = request['trimming']['right']
    )

    s3_upload(
        file_ = TMP_PICTURE_PATH,
        object_name = request['objectName'],
        access_key_id = request['uploader']['aws']['accessKeyId'],
        secret_access_key = request['uploader']['aws']['secretAccessKey'],
        bucket = request['uploader']['aws']['s3Bucket'],
        region = request['uploader']['aws']['region'],
    )
