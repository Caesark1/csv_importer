from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Customer
from .resources import CustomerResources
from tablib import Dataset
import io
import csv


def upload_file(request):
    if request.method == "POST":
        customer_resource = CustomerResources
        dataset = Dataset()
        new_dataset = request.FILES["file"]

        if not new_dataset.name.endswith(".csv"):
            messages.info(request, "wrong file format. Back to the Main page and try again")
            return render(request, "upload_csv.html")
        
        imported_data = dataset.load(new_dataset.read().decode("UTF-8"), format = "csv")
        for column in imported_data:
            value = Customer(
                customer = column[0],
                item = column[1],
                total = column[2],
                quantity = column[3],
                date = column[4]
            )
            value.save()

    return render(request, "upload_csv.html")

class CustomerListView(ListView):
    model = Customer
    template_name = "customer_list.html"
    context_object_name = "customers"


class TopCustomersView(ListView):
    model = Customer
    template_name = "leaderboard.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        leaders = Customer.objects.all().order_by("-total")[:5]
        context["leaders"] = leaders
        return context