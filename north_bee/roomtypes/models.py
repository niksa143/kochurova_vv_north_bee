from django.db import models

class Roomtype(models.Model):
    roomtype_name=models.CharField(max_length=20,verbose_name="Класс номера")
