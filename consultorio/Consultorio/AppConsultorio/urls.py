from django.urls import path
from AppConsultorio import views

urlpatterns = [
    path('',views.inicio,name="inicio"),
]