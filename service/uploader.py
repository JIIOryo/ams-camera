import traceback

import boto3

class S3UploadError(Exception):
    def __init__(self, error, message):
        self.error = error
        self.message = message
    pass

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
        error_detail = ''.join(traceback.TracebackException.from_exception(e).format())
        raise S3UploadError(error, 's3_upload error: ' + error_detail)

    return
