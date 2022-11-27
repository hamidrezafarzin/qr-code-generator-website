from django.urls import path, include 
from QrCodeGeneratorApp import views
urlpatterns = [
    path('generator/', views.QrcodeCreateView.as_view(template_name="index.html")),

]
