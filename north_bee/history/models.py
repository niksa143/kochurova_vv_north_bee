from django.db import models

class History(models.Model):
    check_in=models.DateField(verbose_name="Дата заезда")
    check_out=models.DateField(verbose_name="Дата выезда")
    comment=models.CharField(max_length=100,verbose_name="Комментарий")
    quest = models.ForeignKey("quests.Quest", on_delete=models.CASCADE, verbose_name="Гость")
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, verbose_name="Комната")

    class Meta:

        ordering = ["-check_in"]

