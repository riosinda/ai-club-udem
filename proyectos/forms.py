# proyectos/forms.py
from django import forms
from dal import autocomplete
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'autores': autocomplete.ModelSelect2Multiple(
                url='autor-autocomplete'
            )
        }
