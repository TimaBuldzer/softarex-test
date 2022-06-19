from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.autoencoder.forms import CreateCaseForm


class AutoEncodeView(LoginRequiredMixin, CreateView):
    template_name = 'autoencoder/autoencode.html'
    login_url = '/login/'
    success_url = reverse_lazy('autoencoder:success')
    form_class = CreateCaseForm

    def get_form(self, form_class=None):
        return self.form_class(self.request.POST, self.request.FILES, request=self.request)
