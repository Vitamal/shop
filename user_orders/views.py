from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers.user import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('registration_date',)

