from django.db import models
from datetime import  timedelta
from datetime import datetime
date_format = "%Y-%m-%d"



import time

Equipment_type_choice = (('Reachtruck', 'Reachtruck'), ('PPT', 'PPT'))


# Create your models here.

class Calibration(models.Model):
    Equipment_type = models.CharField(max_length=50, blank=True, null=True, choices=Equipment_type_choice)
    Supplier = models.CharField(max_length=50, blank=True, null=True)
    Manufacturer = models.CharField(max_length=50, blank=True, null=True)
    Owner = models.CharField(max_length=50, blank=True, null=True)
    Internal_code = models.CharField(max_length=50, blank=True, null=True)
    Model = models.CharField(max_length=50, blank=True, null=True)
    Serial_number = models.CharField(max_length=50, blank=True, null=True)
    certificate_status = models.CharField(max_length=50, blank=True, null=True)
    Calibration_status = models.CharField(max_length=50, blank=True, null=True)
    Last_Calibration_Date = models.CharField(max_length=50, blank=True, null=True)
    Duration = models.DurationField(default=timedelta(days=180))
    Expiry_Date = models.CharField(max_length=50, blank=True, null=True)




    def __str__(self):
        return self.Equipment_type





