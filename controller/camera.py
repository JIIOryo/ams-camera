import sys

import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from service.camera import take_picture
from service.trimming import trimming
from service.uploader import s3_upload, publish_picture
from lib.config import get_config_item

TMP_BASE_PICTURE_PATH = get_config_item('tmp_base_picture_path')
TMP_TRIMMED_PICTURE_PATH = get_config_item('tmp_trimmed_picture_path')

def picture(request: dict) -> None:

    # case no camera
    if len(request['cameras']) == 0:
        return

    take_picture(
        file_ = TMP_BASE_PICTURE_PATH,
        x = request['resolution']['x'],
        y = request['resolution']['y'],
        warm_up_time = request['cameraWarmUpTime']
    )

    for camera in request['cameras']:
        trimming(
            input_path = TMP_BASE_PICTURE_PATH,
            output_path = TMP_TRIMMED_PICTURE_PATH,
            top = camera['trimming']['top'],
            bottom = camera['trimming']['bottom'],
            left = camera['trimming']['left'],
            right = camera['trimming']['right']
        )

        if 'mqtt' in request['uploader']:
            publish_picture(
                file_ = TMP_TRIMMED_PICTURE_PATH,
                host = request['uploader']['mqtt']['host'],
                port = request['uploader']['mqtt']['port'],
                user_name = request['uploader']['mqtt']['userName'],
                password = request['uploader']['mqtt']['password'],
                retain = request['uploader']['mqtt']['retain'],
                topic = camera['topic'],
            )

        if 'aws' in request['uploader']:
            s3_upload(
                file_ = TMP_TRIMMED_PICTURE_PATH,
                object_name = camera['objectName'],
                access_key_id = request['uploader']['aws']['accessKeyId'],
                secret_access_key = request['uploader']['aws']['secretAccessKey'],
                bucket = request['uploader']['aws']['s3Bucket'],
                region = request['uploader']['aws']['region'],
            )
