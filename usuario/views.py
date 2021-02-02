from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from usuario.forms import UsuarioForm


class RegistroUsuario(CreateView):
    model = User
    template_name = "formulario_usuario.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('listar')


class ListarUsuarios(ListView):
    model = User
    template_name = 'listar_usuarios.html'


class ActualizarUsuario(UpdateView):
    model = User
    form_class = UsuarioForm
    template_name = 'formulario_usuario.html'
    success_url = reverse_lazy('listar')


class EliminarUsuario(DeleteView):
    model = User
    template_name = 'eliminar_usuario.html'
    success_url = reverse_lazy('listar')
