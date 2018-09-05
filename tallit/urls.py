from django.urls import include, path

from . import views

urlpatterns = [
    path('hopeapaju/', include('tallit.hopeapaju.urls', namespace='hopeapaju')),
    path('', views.index, name='index')
]