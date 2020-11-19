# user_order/urls.py

from django.urls import include, path
from rest_framework import routers
from . import viewsets
from .views import UserList

router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('user_list/', UserList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
