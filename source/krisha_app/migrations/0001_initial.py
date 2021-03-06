# Generated by Django 3.1.1 on 2020-10-06 01:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calibration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Equipment_type', models.CharField(blank=True, choices=[('Reachtruck', 'Reachtruck'), ('PPT', 'PPT')], max_length=50, null=True)),
                ('Supplier', models.CharField(blank=True, max_length=50, null=True)),
                ('Manufacturer', models.CharField(blank=True, max_length=50, null=True)),
                ('Owner', models.CharField(blank=True, max_length=50, null=True)),
                ('Internal_code', models.CharField(blank=True, max_length=50, null=True)),
                ('Model', models.CharField(blank=True, max_length=50, null=True)),
                ('Serial_number', models.CharField(blank=True, max_length=50, null=True)),
                ('certificate_status', models.CharField(blank=True, max_length=50, null=True)),
                ('Calibration_status', models.CharField(blank=True, max_length=50, null=True)),
                ('Last_Calibration_Date', models.CharField(blank=True, max_length=50, null=True)),
                ('Duration', models.DurationField(default=datetime.timedelta(days=180))),
                ('Expiry_Date', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
