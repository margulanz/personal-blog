from django.urls import include, path
from .views import PostViewSet



urlpatterns = [
    path('<int:id>/',PostViewSet.as_view({'get':'retrieve'}),name = 'post-detail'),
    path('',PostViewSet.as_view({'get':'list'}),name = 'posts'),
]