import boto3

def s3_upload(
    file_: str,
    object_name: str,
    access_key_id: str,
    secret_access_key: str,
    bucket: str,
    region: str
) -> None:
    s3_client = boto3.client(
        's3',
        aws_access_key_id = access_key_id,
        aws_secret_access_key = secret_access_key,
        region_name = region,
    )
    response = s3_client.upload_file(
        file_,
        bucket,
        object_name
    )
    print(response)
    return
