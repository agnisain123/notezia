from .views import NotesAPI
from django.urls import path

urlpatterns = [
    path('', NotesAPI.as_view()),
]