from django.db import models
from django.core.validators import MinLengthValidator

from petstagram.pets.models import Pet
from petstagram.photos.validators import ImageSizeValidator

# Create your models here.

class Photo(models.Model):
    photo = models.ImageField(
        upload_to='petPhotos/',
        validators=[ImageSizeValidator(5, 'MB', 'The maximum image size can that be uploaded is 5Mb.')]
    )

    description = models.TextField(
        max_length=300,
        validators=[MinLengthValidator(10)],
        null=True,
        blank=True,
    )

    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )
