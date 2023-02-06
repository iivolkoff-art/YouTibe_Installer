from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('install/', views.second_page, name='installer')
]