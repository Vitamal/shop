from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

from user_orders.filters import RegistrationDateFilter
from user_orders.serializers.user import UserSerializer
from user_orders.models import User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RegistrationDateFilter

    def get_queryset(self):
        return User.objects.all().order_by('id')
