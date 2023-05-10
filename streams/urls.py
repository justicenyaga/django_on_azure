from django.urls import path
from . import views

urlpatterns = [
    path('', views.getStreams, name="streams"),
    path('<str:pk>/', views.getStream, name="stream"),
]
