from django.core.management.base import BaseCommand
from openpyxl import load_workbook
from core.models import Students


class Command(BaseCommand):
    help = 'Import Excel data into the database'
    headers = []

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        workbook = load_workbook(filename=file_path)
        sheet = workbook.active
        for index, row in enumerate(sheet.rows):
            # Get headers
            if index == 0:
                self.headers = [str(cell.value).lower().replace(" ", "_") for cell in row]
            # get values
            else:
                values = [cell.value if cell.value else "" for cell in row]
                # kwargs = dict(zip(self.headers, values))
                student = Students()
                for key, value in zip(self.headers, values):
                    setattr(student, key, value)
                student.save()
                self.stdout.write(self.style.SUCCESS(f'\rSuccessfully imported row {index}'), ending='')

        self.stdout.write(self.style.SUCCESS('Data import completed.'))
