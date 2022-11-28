from django.urls import path, include 
from QrCodeGeneratorApp import views

urlpatterns = [
    path('generator/', views.Qr_code_Create_View, name="fbv_view"),

]
