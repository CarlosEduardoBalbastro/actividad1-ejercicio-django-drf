from django.urls import path

from .views import decir_hola



urlpatterns = [
    path('', decir_hola),
]