from django import forms


from quests.models import Quest


class QuestForm(forms.ModelForm):


    class Meta:

        model = Quest
        fields = "__all__"
        widgets = {
            "birthday": forms.DateInput(format="%Y-%m-%d",

                                        attrs={"type": "date"}),

        }
