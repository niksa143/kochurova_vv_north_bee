from django.db import models

from django.urls import reverse_lazy

class Quest(models.Model):
    full_name=models.CharField(max_length=100,verbose_name="Полное имя")
    birthday=models.DateField(verbose_name="Дата рождения")
    gender=models.ForeignKey("genders.Gender",on_delete=models.CASCADE,verbose_name="Пол")
    status=models.ForeignKey("status.Status",on_delete=models.CASCADE,verbose_name="Статус")

    def __str__(self):
        return f"{self.full_name}"

    def get_visits_count(self):
        # PKGH Подсчет выручки ваодителя.

        return self.history_set.count()

    def get_update_url(self):
        return reverse_lazy("quest-update",kwargs={"pk":self.pk})

    def get_history_url(self):
        return reverse_lazy("quest-history",kwargs={"pk":self.pk})


    class Meta:
        ordering=["full_name"]