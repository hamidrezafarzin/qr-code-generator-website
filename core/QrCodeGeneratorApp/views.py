from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse

# Create your views here.

class QrcodeCreateView(TemplateView):
    template_name="index.html"
    pass