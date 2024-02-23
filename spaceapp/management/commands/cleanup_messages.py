from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from spaceapp.models import UserMessage

class Command(BaseCommand):
    help = 'Deletes UserMessage records older than a specified number of days'

    def add_arguments(self, parser):
        parser.add_argument('days', type=int, help='Age of messages in days to retain')

    def handle(self, *args, **kwargs):
        days = kwargs['days']
        cutoff_date = timezone.now() - timedelta(days=days)
        count, _ = UserMessage.objects.filter(created_at__lt=cutoff_date).delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} old records.'))


'''
python manage.py shell -c "from spaceapp.models import UserMessage; message=UserMessage.objects.first(); message.delete() if message else print('No message to delete')"
'''