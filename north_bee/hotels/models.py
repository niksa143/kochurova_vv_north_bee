from django.db import models

class Hotel(models.Model):
    hotel_name=models.CharField(max_length=30,verbose_name="Название отеля")
    
