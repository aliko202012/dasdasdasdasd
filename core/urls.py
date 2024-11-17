from django.contrib import admin
from django.urls import path
from apps.base.views import *
from rest_framework.routers import DefaultRouter





router = DefaultRouter()
router.register('api_recipe',RecipeAPI,basename='api_and_mixins_recipe')

urlpatterns = [
    path('admin/', admin.site.urls)

]

urlpatterns += router.urls