# cards/forms.py

from django import forms
from numpy import require


class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)