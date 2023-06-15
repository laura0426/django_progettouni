from django import forms
from .models import Ricette


class RicettaForm(forms.ModelForm):
    class Meta:
        model = Ricette
        fields = ('nome', 'ingredienti', 'procedimento', 'tempo', 'difficolta', 'categoria')

