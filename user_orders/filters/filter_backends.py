from django_filters import rest_framework as filters

from user_orders.models import User


class RegistrationDateFilter(filters.FilterSet):
    """
    Filtering users by registration date.
    """
    min_registration_date = filters.DateFilter(field_name="registration_date", lookup_expr='gte')
    max_registration_date = filters.DateFilter(field_name="registration_date", lookup_expr='lte')

    class Meta:
        model = User
        fields = ['registration_date']
