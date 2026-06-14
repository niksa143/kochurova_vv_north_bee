from django.db import models

class Room(models.Model):
    number=models.CharField(max_length=5,verbose_name="Номер комнаты")
    hotel = models.ForeignKey("hotels.Hotel", on_delete=models.CASCADE, verbose_name="Отель")
    roomtype=models.ForeignKey("roomtypes.Roomtype",on_delete=models.CASCADE,verbose_name="Класс номера")
