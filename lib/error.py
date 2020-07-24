
class S3UploadError(Exception):
    def __init__(self, error, message):
        self.error = error
        self.message = message
    pass