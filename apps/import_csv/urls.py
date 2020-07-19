from django.urls import path
from .views import *

urlpatterns = [
    path("",  upload_file, name = "upload"),
    path("customers/", CustomerListView.as_view(), name = "customers"),
    path("learboard/", TopCustomersView.as_view(), name = "leaderboard")
]