from django.core.management.base import BaseCommand
from openpyxl import Workbook
from core.models import Students


class Command(BaseCommand):
    help = 'Export data from the database into an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        headers = [field.name for field in Students._meta.fields]
        rows = Students.objects.values_list(*headers)

        workbook = Workbook()
        sheet = workbook.active

        # Write headers
        sheet.append(headers)

        # Write rows
        for row in rows:
            sheet.append(row)

        workbook.save(file_path)

        self.stdout.write(self.style.SUCCESS(f'[✔] Data exported to Excel: {file_path}'))

