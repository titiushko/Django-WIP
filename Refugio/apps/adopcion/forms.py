from django import forms
from apps.adopcion.models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona

        fields = '__all__'

        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'edad': 'Edad',
            'telefono': 'Teléfono',
            'email': 'Email',
            'domicilio': 'Domicilio'
        }

        widgets = {
            'nombres': forms.TextInput(attrs = { 'class': 'form-control' }),
            'apellidos': forms.TextInput(attrs = { 'class': 'form-control' }),
            'edad': forms.NumberInput(attrs = { 'class': 'form-control' }),
            'telefono': forms.TextInput(attrs = { 'class': 'form-control' }),
            'email': forms.EmailInput(attrs = { 'class': 'form-control' }),
            'domicilio': forms.Textarea(attrs = { 'class': 'form-control' }),
        }
