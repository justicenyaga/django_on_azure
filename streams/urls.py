from django.urls import path
from . import views

urlpatterns = [
    path('', views.getStreams, name="streams"),
    path('create/', views.createStream, name='stream-create'),
    path('<str:pk>/', views.getStream, name="stream"),
]
