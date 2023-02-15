from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ImageSerializer
import os
from .models import Image
from uuid import uuid4
from backend.settings import MEDIA_ROOT, MEDIA_URL

class ImageAPIView(APIView):
    #view images
    def get(self, request, id) :
        image = Image.objects.filter(day = id)
        serializer = ImageSerializer(image, many=True)

        media_name = serializer.data[0].get("uuid_name")
        image_url = os.path.join(MEDIA_URL, media_name)
        response = {
            'image_url': image_url
        }
        print(response)
        return Response(response)



    def post(self, request):

        # 일단 파일 불러와
        image = request.FILES.get('image')
        name = image.name
        print(1)

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        save_path += '.jpg'
        #save file
        with open(save_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

        print(1)

        serializer = ImageSerializer(data={'name':name, 'day':1, 'uuid_name':uuid_name}) #use dict for creating

        if serializer.is_valid() :
            print(1)
            serializer.save()
        
        return Response(status=200)