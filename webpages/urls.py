from django.urls import path
from .views import PessoaAPIView

urlpatterns = [
    path('pessoas/', PessoaAPIView.as_view(), name='pessoas'),
]
