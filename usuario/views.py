from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from usuario.forms import UsuarioForm


class RegistroUsuario(CreateView):
    model = User
    template_name = "registrar_usuario.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('mascota_listar_clases')
