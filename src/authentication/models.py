from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(
        max_length=255, help_text='User bio', null=False, blank=True,
        default=''
    )
