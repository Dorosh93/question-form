from django.urls import path
from . import views

app_name = 'form'

urlpatterns = [
    path('', views.question_create, name='question_create'),
]