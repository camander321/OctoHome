from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='videos-home'),
    path('help/', views.help, name='videos-help'),
    #path('jsontest/', views.jsonTest, name='videos-jsontest'),
]
