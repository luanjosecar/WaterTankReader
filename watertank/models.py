from django.db import models

# Create your models here.
class Tanks(models.Model):
    identification = models.CharField(max_length=200)
    user_identification = models.CharField(max_length=200)
    status = models.BooleanField(default=False)


class Users(models.Model):
    user_id = models.CharField(max_length=200)