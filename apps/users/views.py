from django.contrib.auth import views
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.users.forms import UserRegisterForm, UserUpdateForm


class LoginView(views.LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        return '/'


class RegisterView(CreateView):
    template_name = 'auth/register.html'
    success_url = reverse_lazy('users:login')
    form_class = UserRegisterForm


class ProfileView(UpdateView):
    template_name = 'auth/profile.html'
    success_url = '/'
    form_class = UserUpdateForm

    def get_object(self, queryset=None):
        return self.request.user
