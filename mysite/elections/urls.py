from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('areas/<str:area>/', views.areas),
]
