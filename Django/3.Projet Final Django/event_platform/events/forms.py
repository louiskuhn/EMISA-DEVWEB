from django import forms
from .models import Event
from django.forms.widgets import TextInput

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'capacity', 'image']
        widgets = {
            'date': TextInput(attrs={
                'id': 'id_date',      # Pour pouvoir cibler l'input avec Flatpickr
                'class': 'form-control',
                'placeholder': 'Sélectionnez une date et une heure'
            }),
        }

