from django import forms
from django.forms import ModelForm
from .models import Note, Category


CHOICES1 = (("date", "Created"), ("title", "Alphabetical"), ("last", "Last Modified"))

CHOICES2 = ((" ", "Ascending"), ("-", "Descending"))

a = Category.objects.all()

OPTION = [(i.sector, i.sector) for i in a]

OPTION = tuple(OPTION)

class CreateForm(ModelForm):
    class Meta:
        model = Note
        fields = ["title", "text", "name"]


class OrderForm(forms.Form):
    order = forms.ChoiceField(choices=CHOICES1, label=False, initial=CHOICES1[0])
    sequence = forms.ChoiceField(choices=CHOICES2, label=False, initial=CHOICES2[1])

class SectorForm(forms.Form):
    sec = forms.ChoiceField(choices=OPTION, label=False)