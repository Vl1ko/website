from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('response/', views.response, name="response_page"),
]