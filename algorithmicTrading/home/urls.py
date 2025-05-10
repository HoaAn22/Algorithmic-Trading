from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home),
    path('env/', views.get_env),
]