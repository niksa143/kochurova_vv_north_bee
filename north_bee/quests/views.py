from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView


from quests.forms import QuestForm

from quests.models import Quest


class QuestUpdateView(SuccessMessageMixin,

                       UpdateView):

    model = Quest

    form_class = QuestForm

    success_url = reverse_lazy("home")

    success_message = "Информация о госте сохранена"

class QuestCreateView(SuccessMessageMixin,

                       CreateView):

    model = Quest
    form_class = QuestForm

    success_url = reverse_lazy("home")

    success_message = "Информация о госте добавлена"
