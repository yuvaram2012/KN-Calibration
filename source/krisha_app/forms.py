from django import forms
from .models import Calibration


class StockCreateForm(forms.ModelForm):

    class Meta:
        model = Calibration
        fields = ['Equipment_type', 'Supplier', 'Manufacturer', 'Owner', 'Internal_code', 'Model',
                  'Serial_number','Last_Calibration_Date']

