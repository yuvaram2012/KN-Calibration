from django.contrib import admin
from .models import Calibration
from.forms import StockCreateForm


class StockCreateFormAdmin(admin.ModelAdmin):
    list_display = ['Equipment_type','Supplier', 'Manufacturer', 'Owner', 'Internal_code', 'Model','Serial_number',
                    'Calibration_status',
                    'certificate_status']
    form = StockCreateForm
    list_filter = ['Equipment_type', 'Internal_code','Calibration_status', 'certificate_status']
    search_fields = ['Equipment_type', 'Internal_code','Calibration_status', 'certificate_status']


admin.site.register(Calibration, StockCreateFormAdmin)

