from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


def validate_file_extension(value):
    if not value.name.endswith('.png'):
        raise ValidationError('You can upload only .png files')


class Case(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original = models.ImageField(upload_to='cases/original/%Y/%m/%d', validators=[validate_file_extension])
    encoded = models.ImageField(upload_to='cases/encoded/%Y/%m/%d', null=True, validators=[validate_file_extension])
