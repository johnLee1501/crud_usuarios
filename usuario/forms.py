from django import forms
from django.contrib.auth.models import User


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password']
        labels = {
            "username": "Usuario",
            "first_name": "Nombre",
            "email": "Correo",
            "password": "Constraseña"
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }
