from django.shortcuts import render
from rest_framework.views import APIView

from .serializer import DaySerializer
from .models import Day
from rest_framework.response import Response
# Create your views here.
class DayAPIView(APIView):
    def get(self, request):
        days = Day.objects.all()
        serializer = DaySerializer(days, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DaySerializer(data=request.data)

        if serializer.is_valid() :
            serializer.save()
        print(serializer)
        return Response(serializer.data)