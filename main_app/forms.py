from . import models
from django import forms


class AdherentForm(forms.ModelForm):
    class Meta:
        model = models.Adherent
        fields = ['prenom', 'nom', 'username', 'Email', 'password', 'adresse', 'genre', 'tel']


