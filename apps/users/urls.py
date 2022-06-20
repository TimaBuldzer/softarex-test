from django.contrib.auth.views import LogoutView
from django.urls import path
from apps.users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout')
]
