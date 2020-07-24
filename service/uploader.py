import traceback
import sys
import subprocess

import boto3

import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from lib.error import (
    S3UploadError,
)

def s3_upload(
    file_: str,
    object_name: str,
    access_key_id: str,
    secret_access_key: str,
    bucket: str,
    region: str
) -> dict:
    s3_client = boto3.client(
        's3',
        aws_access_key_id = access_key_id,
        aws_secret_access_key = secret_access_key,
        region_name = region,
    )
    try:
        response = s3_client.upload_file(
            file_,
            bucket,
            object_name
        )
    except Exception as e:
        error = e.__class__.__name__
        error_detail = 's3_upload error: ' + ''.join(traceback.TracebackException.from_exception(e).format())
        raise S3UploadError(error, error_detail)

    return

def puclish_picture(
    file_: str,
    host: str,
    port: int,
    user_name: str,
    password: str,
    retain: bool,
    topic: str,
) -> None:

    cmd = f'mosquitto_pub -h {host} -p {port} '
    if len(user_name) and len(password): cmd += f'-u {user_name} -P {password} '
    cmd += f'-t {topic} -f {file_}'
    if retain: cmd += '-r '

    subprocess.run(cmd.split())
    return
