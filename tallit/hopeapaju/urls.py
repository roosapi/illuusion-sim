from django.urls import path

from . import views

urlpatterns = [
    path('hevoset/<slug>', views.horse, name='horse'),
    path('hevoset', views.horses, name='all-horses'),
]