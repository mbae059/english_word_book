from django.shortcuts import render
from rest_framework.views import APIView

from .serializer import WordSerializer
from .models import Word
from rest_framework.response import Response
# Create your views here.
class WordAPIView(APIView):
    def get(self, request, id):
        # get queryset of words by filtering day
        words = Word.objects.filter(day = id)
        # get list of words by using serializer and many options
        # each element of the list will be json
        serializer = WordSerializer(words, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = WordSerializer(data=request.data)
        
        if serializer.is_valid() :
            serializer.save()
        return Response(serializer.data)


    def put(self, request, id):
        word = Word.objects.get(id=id)
        serializer = WordSerializer(word, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        word = Word.objects.get(id=id)
        word.delete()
        return Response(status=200)