from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from apps.autoencoder.forms import CreateCaseForm
from apps.autoencoder.models import Case
from apps.autoencoder.selectors import get_cases


class AutoEncodeView(LoginRequiredMixin, CreateView):
    template_name = 'autoencoder/autoencode.html'
    login_url = '/login/'
    success_url = reverse_lazy('autoencoder:cases')
    form_class = CreateCaseForm

    def get_form(self, form_class=None):
        return self.form_class(self.request.POST, self.request.FILES, request=self.request)


class AutoEncodedCasesView(LoginRequiredMixin, ListView):
    template_name = 'autoencoder/autoencode_cases.html'
    login_url = '/login/'
    model = Case

    def get_queryset(self):
        return get_cases(user=self.request.user)
