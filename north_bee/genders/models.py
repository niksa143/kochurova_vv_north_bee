from django.db import models

class Gender(models.Model):
    gender_name=models.CharField(max_length=20,verbose_name="Пол")

    def __str__(self):
        return self.gender_name
