from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

# Create your views here.
class NotesAPI(APIView):
    def post (self, request):
        note=NoteSerializer(data=request.data)
        note.is_valid(raise_exception=True)
        note.save()
        return Response(note.data)

    def get (self, request):
        notes=Note.objects.filter()
        noteData=NoteSerializer(data=notes, many=True)
        return Response(noteData.data)