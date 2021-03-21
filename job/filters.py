import django_filters
from .models import Job


class JobFilters(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains')
    descripyion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['image','slug','onwer']