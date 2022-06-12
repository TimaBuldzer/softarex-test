from django.contrib.auth import views


class LoginView(views.LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        return '/'
