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
        noteData=NoteSerializer(notes, many=True)
        return Response(noteData.data)

class UserAPI(APIView):
    def post (self, request, route):
        password = request.data['password']
        note = Note.objects.filter(route=route)
        if not note:
            return Response({'message': 'Invalid Note'}) 
        serializedNote = NoteSerializer(note[0])
        if serializedNote.data['password'] != password:
            return Response({'message': 'Incorrect Password'}) 
        return Response({ 'note': serializedNote.data })   

    def get (self, request, route):
        note = Note.objects.filter(route=route)
        if not note:
            return Response({'message': 'Route does not exist'}) 
        else:
            return Response({'message': 'Route Exists'}) 

    