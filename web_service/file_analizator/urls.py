from django.urls import path
from . import views

urlpatterns = [
    path('file', views.upload_file, name='file'),
    path('', views.home_page, name='home')
]
