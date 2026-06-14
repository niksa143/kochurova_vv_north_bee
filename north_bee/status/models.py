from django.db import models

class Status(models.Model):
    status_name=models.CharField(max_length=20,verbose_name="Статус")

