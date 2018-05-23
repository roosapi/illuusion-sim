from django.urls import include,path

from . import views

urlpatterns = [
    path('hopeapaju/', include('tallit.hopeapaju.urls')),
    path('', views.index, name='index')
]