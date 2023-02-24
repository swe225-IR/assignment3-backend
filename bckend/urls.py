from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from bckend import views

router = DefaultRouter()
# router.register('bckend', views.ResultViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path(r'query', get_results)
]
