from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('api_book',BookAPI,basename='api_and_mixins_book')

urlpatterns = [

]

urlpatterns += router.urls