from django.db import models

class Gender(models.Model):
    gender_name=models.CharField(max_length=20,verbose_name="Пол")

