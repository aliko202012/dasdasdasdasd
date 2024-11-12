from django.shortcuts import render
# from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .serializers import BookSerializers
from .models import Book
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class Pagination(PageNumberPagination):
    page_size = 10
    max_page_size = 10

class BookAPI(GenericViewSet,
              mixins.CreateModelMixin,
              mixins.DestroyModelMixin,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializers
    pagination_class = Pagination