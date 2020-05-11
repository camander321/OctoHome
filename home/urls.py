from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home-home'),
    path('help/', views.help, name='home-help'),
    #path('jsontest/', views.jsonTest, name='home-jsontest'),
]
