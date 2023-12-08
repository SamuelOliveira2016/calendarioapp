from django.shortcuts import render
# Create your views here.


from django.views.generic import ListView
#from .models import Areatecnologica, Pessoa, Planocurso, Professor, Vinculo, HoratrabProf, Tipocurso, Calendario


class HomePageView(ListView):
 #model = Areatecnologica
 template_name = "home.html"

class AboutPageView(ListView):
 #model = Pessoa
 template_name = "about.html"

