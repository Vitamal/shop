from rest_framework import serializers

from user_orders.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'registration_date', 'order']
