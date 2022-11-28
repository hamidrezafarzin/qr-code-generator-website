from django.urls import path, include 
from QrCodeGeneratorApp import views

app_name = 'QrCodeGeneratorApp'

urlpatterns = [
    path('fbv-generator/', views.Qr_code_Create_View, name="fbv_view"),
    path('api/', include('QrCodeGeneratorApp.api.urls')),

]
