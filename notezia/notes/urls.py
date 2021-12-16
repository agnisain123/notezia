from .views import NotesAPI, UserAPI, landing, note
from django.urls import path

urlpatterns = [
    path('api/', NotesAPI.as_view()),
    path('<str:route>/', UserAPI.as_view()),
    path('', landing, name="index"),
    path("note/", note, name="note")
]