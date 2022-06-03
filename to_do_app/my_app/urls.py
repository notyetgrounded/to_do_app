from django.urls import path
from . import views
from .views import *

urlpatterns=[
    path('todo/',ToDoAPI.as_view()),
    path('register/',RegisterUser.as_view())
]
