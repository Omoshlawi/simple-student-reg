# Generated by Django 4.2.2 on 2023-06-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('tt_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('id_number', models.CharField(max_length=50)),
                ('centre_code', models.CharField(max_length=50)),
                ('centre_name', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=50)),
                ('trade_code', models.CharField(max_length=50)),
                ('trade_name', models.CharField(max_length=50)),
                ('test_series', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=50)),
                ('photo_link', models.CharField(max_length=50)),
            ],
        ),
    ]
