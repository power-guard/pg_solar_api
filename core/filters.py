import django_filters
from .models import LoggerPowerGen, LoggerCategory
from django.utils.dateparse import parse_date
from datetime import timedelta

class LoggerPowerGenFilter(django_filters.FilterSet):
    year_month = django_filters.CharFilter(method='filter_by_year_month')
    logger_name = django_filters.CharFilter(method='filter_by_logger_names')

    class Meta:
        model = LoggerPowerGen
        fields = ['year_month', 'logger_name']

    def filter_by_year_month(self, queryset, name, value):
        try:
            year, month = map(int, value.split('-'))
            start_date = f'{year}-{month:02d}-01'
            end_date = f'{year}-{month:02d}-31'

            start_date = parse_date(start_date)
            end_date = parse_date(end_date)

            # Adjust end date to the last day of the month if necessary
            if end_date.month != month:
                end_date = end_date.replace(day=1) + timedelta(days=-1)

            return queryset.filter(date__range=[start_date, end_date])
        except ValueError:
            return queryset.none()

    def filter_by_logger_names(self, queryset, name, value):
        # Split the comma-separated list of logger names
        names = value.split(',')
        # Filter LoggerCategory by the provided logger names
        categories = LoggerCategory.objects.filter(logger_name__in=names)
        return queryset.filter(logger_name__in=categories)
