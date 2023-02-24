from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bckend.views import *

router = DefaultRouter()

urlpatterns = [
    path(r'query', get_results)
]
