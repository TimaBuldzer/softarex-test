from django.contrib.auth import views
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.users.forms import UserRegisterForm


class LoginView(views.LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        return '/'


class RegisterView(CreateView):
    template_name = 'auth/register.html'
    success_url = reverse_lazy('users:login')
    form_class = UserRegisterForm
