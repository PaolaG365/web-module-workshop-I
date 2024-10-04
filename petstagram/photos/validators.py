from typing import Any
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ImageSizeValidator:
    """Image size validator
    Args:
        limit: in integers, size limit for the file
        data_size_type: unit of size (B, KB, MB, GB, TB)
        message: custom error message if validation fails
    """
    FILE_SIZE_MAP = {   
    "B": 1,
    "KB": 1024,
    "MB": 1024 ** 2,
    "GB": 1024 ** 3,
    "TB": 1024 ** 4,
}

    def __init__(self, limit: int, data_size_type: str, message='Image size exceeds set limit'):
        self.limit = limit
        self.data_size_type = data_size_type
        self.message= message

    def __call__(self, file):
        if file.size > self.limit * ImageSizeValidator.FILE_SIZE_MAP[self.data_size_type]:
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'petstagram.photos.validators.ImageSizeValidator',
            (),
            {
                'limit': self.limit,
                'data_size_type': self.data_size_type,
                'message': self.message,
                }
        )

