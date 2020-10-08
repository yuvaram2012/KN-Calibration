from django.shortcuts import render, redirect
from .models import *
from.forms import StockCreateForm
from .my_mailing import send_email, send_email_at
import datetime as dt
import time
date_format = "%Y-%m-%d"




# Create your views here.


def home(request):
    body = 'Welcome Home page'
    context = {
     "body": body,
    }

    return render(request, "home.html", context)





def items(request):
    title = 'list of items'


    queryset = Calibration.objects.all()
    context = {

        "title": title,
        "queryset": queryset,
    }

    return render(request, "items.html", context)


def add_items(request):
    form = StockCreateForm(request.POST or None)

    if form.is_valid():
        string = request.POST["Last_Calibration_Date"]
        Last_Calibration_Date = datetime.strptime(string, "%d-%m-%Y")
        form.instance.Last_Calibration_Date = Last_Calibration_Date
        Expiry_Date=Last_Calibration_Date+timedelta(days=180)
        form.instance.Expiry_Date = Expiry_Date


        if Expiry_Date<=datetime.now():
            Calibration_status='Expired'
            form.instance.Calibration_status = Calibration_status
            form.save()
            form.send_email=send_email
        else:
            Calibration_status = 'Active'
            form.instance.Calibration_status = Calibration_status
            form.save()


        return redirect('/items')
    context = {
     "form": form
    }
    return render(request, "add_items.html", context)


