from django.shortcuts import render
from django.http import HttpResponse
# from .models import 
# from AppConsultorio.forms import 

def inicio(request):
    return render(request,"AppConsultorio/index.html")