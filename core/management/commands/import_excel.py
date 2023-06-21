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

        # Loop through the DataFrame rows and save them as model instances
        for index, row in enumerate(sheet.rows):
            # my_model = MyModel(
            #     # Assign column values to model fields
            #     field1=row['Column1'],
            #     field2=row['Column2'],
            #     # Add more fields as necessary
            # )
            # my_model.save()
            # self.stdout.write(self.style.SUCCESS(f'Successfully imported row {index + 1}'))\
            # Get headers
            if index == 0:
                self.headers = [(cell.value).lower().replace(" ", "_") for cell in row]
            # get values
            else:
                values = [cell.value if cell.value else "" for cell in row]
                kwargs = dict(zip(self.headers, values))
                print(kwargs)
                return
                # Students.objects.create(**kwargs)
                # self.stdout.write(self.style.SUCCESS(f'Successfully imported row {index}'))

        self.stdout.write(self.style.SUCCESS('Data import completed.'))
