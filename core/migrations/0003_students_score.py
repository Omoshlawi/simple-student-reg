# Generated by Django 4.2.2 on 2023-06-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_students_id_remove_students_institution_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
            preserve_default=False,
        ),
    ]