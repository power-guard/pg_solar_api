from django.core.management.base import BaseCommand
from django.db.models import Sum
from core.models import DevicePowerGen, LoggerPowerGen, LoggerCategory
from datetime import date

class Command(BaseCommand):
    help = 'Aggregate power_gen from DevicePowerGen and save to LoggerPowerGen'

    def handle(self, *args, **kwargs):
        # Get the current date
        current_date = date.today()
        print(date)
        # Aggregate power_gen by logger_name and date
        aggregated_data = DevicePowerGen.objects.filter(date=current_date).values('logger_name').annotate(total_power_gen=Sum('power_gen'))
        
        for data in aggregated_data:
            logger_name = LoggerCategory.objects.get(id=data['logger_name'])
            total_power_gen = data['total_power_gen']
            
            # Create or update LoggerPowerGen entry
            LoggerPowerGen.objects.update_or_create(
                logger_name=logger_name,
                date=current_date,
                defaults={'power_gen': total_power_gen}
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully aggregated and saved power_gen data'))
