import django_filters
from .models import LoggerPowerGen, LoggerCategory
from django.utils.dateparse import parse_date
from datetime import timedelta

class LoggerPowerGenFilter(django_filters.FilterSet):
    year_month = django_filters.CharFilter(method='filter_by_year_month')
    year_month_date = django_filters.CharFilter(method='filter_by_year_month_date')
    logger_name = django_filters.CharFilter(method='filter_by_logger_names')

    class Meta:
        model = LoggerPowerGen
        fields = ['year_month', 'year_month_date', 'logger_name']

    def filter_by_year_month(self, queryset, name, value):
        try:
            year, month = map(int, value.split('-'))
            start_date = f'{year}-{month:02d}-01'
            start_date = parse_date(start_date)

            # Calculate the last day of the month
            next_month = start_date.replace(day=28) + timedelta(days=4)
            end_date = next_month - timedelta(days=next_month.day)

            return queryset.filter(date__range=[start_date, end_date])
        except ValueError:
            return queryset.none()

    def filter_by_year_month_date(self, queryset, name, value):
        try:
            # Check if value has a day part
            parts = value.split('-')
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2]) if len(parts) > 2 else None

            if day:
                # If a day is provided, filter by that specific date
                start_date = f'{year}-{month:02d}-{day:02d}'
                end_date = start_date  # End date is the same as start date
            else:
                # If no day is provided, filter for the entire month
                start_date = f'{year}-{month:02d}-01'
                end_date = (parse_date(start_date).replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)

            start_date = parse_date(start_date)
            end_date = parse_date(end_date)

            return queryset.filter(date__range=[start_date, end_date])
        except (ValueError, TypeError):
            return queryset.none()

    def filter_by_logger_names(self, queryset, name, value):
        # Split the comma-separated list of logger names
        names = value.split(',')
        # Filter LoggerCategory by the provided logger names
        categories = LoggerCategory.objects.filter(logger_name__in=names)
        return queryset.filter(logger_name__in=categories)
