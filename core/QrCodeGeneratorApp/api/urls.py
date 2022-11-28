from django.urls import path, include
from QrCodeGeneratorApp.api import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # FBV Rest
    # path('post/', views.post_list, name="post-list"),
    # path('post/<int:id>/', views.post_detail, name="post-detail"),
    
    path('generator/', views.Generator.as_view(), name="CBV-DRF"),
]
