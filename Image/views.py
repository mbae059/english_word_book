from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ImageSerializer
import os
from uuid import uuid4
from backend.settings import MEDIA_ROOT
from django.http import FileResponse

class ImageAPIView(APIView):
    #view images
    def get(self, request, id) : 
        image_path = MEDIA_ROOT / id
        try:
            response = FileResponse(open(image_path, 'rb'), content_type='image/jpeg')
        except IOError:
            response = Response({'error': 'File not found'})
            response.status_code = 404
        return response


    def post(self, request):

        # 일단 파일 불러와
        image = request.FILES.get('image')
        name = image.name

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        #save file
        with open(save_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)


        serializer = ImageSerializer(name=name, day=1, uuid=uuid_name)

        if serializer.is_valid() :
            serializer.save()
        
        return Response(status=200)