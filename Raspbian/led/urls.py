from django.contrib import admin
from django.urls import path
from led import views

urlpatterns = [
    path('', views.index , name="led"),
    path('turn_on',views.turn_on , name="turn_on"),
    path('turn_off' , views.turn_off, name="turn_off")
]