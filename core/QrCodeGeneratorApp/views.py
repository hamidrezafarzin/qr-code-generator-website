from django.shortcuts import render
from QrCodeGeneratorApp.forms import GeneratorForm
#pip install Django Pillow qrcode
from qrcode import *
from django.conf import settings
import time

# Create your views here.

def Qr_code_Create_View(request):
    if request.method == 'POST':
        form = GeneratorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['text']
            img = make(data)
            img_name = 'qr' + str(time.time()) + '.png'
            img.save(f"{settings.MEDIA_ROOT}/{img_name}")
            context = {
                "result" : img_name
            }
            return render(request, 'index.html', context)
    return render(request, 'index.html')
