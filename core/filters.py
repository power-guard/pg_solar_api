import django_filters
from .models import LoggerPowerGen

class LoggerPowerGenFilter(django_filters.FilterSet):
    # Combine year and month into one filter method
    date_range = django_filters.CharFilter(method='filter_by_date_range')

    logger_name = django_filters.ModelChoiceFilter(queryset=LoggerPowerGen.objects.all())

    class Meta:
        model = LoggerPowerGen
        fields = ['date_range', 'logger_name']

    def filter_by_date_range(self, queryset, name, value):
        try:
            year, month = map(int, value.split('-'))
        except ValueError:
            return queryset.none()
        
        return queryset.filter(
            date__year=year,
            date__month=month
        )
