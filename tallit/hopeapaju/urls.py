from django.urls import path

from . import views

app_name = 'hopeapaju'
urlpatterns = [
    path('hevoset/<slug:slug>/', views.horse, name='horse'),
    path('hevoset/', views.horses, name='allhorses'),
    path('pv/', views.pv, name='pv'),
    path('sh/', views.sh, name='sh'),
    path('<breed>/', views.horselist, name='horselist'),
    path('', views.index, name='index'),
    ]