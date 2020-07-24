
class AmsCameraError(Exception):
    def __init__(self, error, message):
        self.error = error
        self.message = message
    pass

class S3UploadError(AmsCameraError):
    pass

class KeyNotExist(Exception):
    pass
