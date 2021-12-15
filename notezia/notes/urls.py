from .views import NotesAPI, UserAPI
from django.urls import path

urlpatterns = [
    path('', NotesAPI.as_view()),
    path('<str:route>/', UserAPI.as_view())
]