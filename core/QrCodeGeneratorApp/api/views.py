from rest_framework.views import APIView
from QrCodeGeneratorApp.api.serializers import GeneratorSerializer
from rest_framework.response import Response

#pip install Django Pillow qrcode
from qrcode import *
from django.conf import settings
import time

class Generator(APIView):
    serializer_class = GeneratorSerializer

    # def get(self, request):
    #     """retriveing a list of posts"""
    #     serializer = self.serializer_class()
    #     return Response(serializer.data)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():                
            data = serializer.data["text"]
            img = make(data)
            img_name = 'qr' + str(time.time()) + '.png'
            img.save(f"{settings.MEDIA_ROOT}/{img_name}")
            context = {
                "QR_url": f"/media/{img_name}"
            }
            return Response(context)
        else:
            return Response(serializer.errors)