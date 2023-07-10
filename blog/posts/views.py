from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import ListPostSerialzier

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-post_at')
    serializer_class = ListPostSerialzier
    lookup_field = 'id'