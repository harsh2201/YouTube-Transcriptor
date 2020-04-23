from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home),
    path('pro/',views.pro,name='pro'),
    path('jump/',views.jump,name ='jump'),
]
