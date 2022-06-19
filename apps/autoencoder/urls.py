from django.urls import path
from apps.autoencoder import views

app_name = 'autoencoder'

urlpatterns = [
    path('autoencode/', views.AutoEncodeView.as_view(), name='autoencode')
]
