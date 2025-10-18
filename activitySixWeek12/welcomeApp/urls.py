from django.urls import path
from . import views

urlpatterns = [
    path('welcome/<str:name>/', views.welcome, name='welcome'),
]
