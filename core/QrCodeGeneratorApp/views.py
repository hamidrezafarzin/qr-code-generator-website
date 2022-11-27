from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

class QrcodeCreateView(View):
    def get(self, request):
            return HttpResponse('get')
    
    def get(self, request):
                return HttpResponse('post')
        