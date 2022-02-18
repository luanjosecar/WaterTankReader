from django.db import models

# Create your models here.

class Users(models.Model):
    identification = models.CharField(max_length=200)
    user_status = models.BooleanField(default=False)

class Tanks(models.Model):
    identification = models.CharField(max_length=200)
    tank_value = models.FloatField(default=0)
    tank_data = models.DateTimeField(default=0)

class TankUser(models.Model):
    user_identification = models.ForeignKey(Users, on_delete=models.CASCADE)
    tank_identification = models.ForeignKey(Tanks, on_delete=models.CASCADE)