from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .views import Studentviewset

router = DefaultRouter()
router.register(r'students', Studentviewset)

urlpatterns = [
    path('', include(router.urls)), 
]