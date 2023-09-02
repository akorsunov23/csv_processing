from django.urls import path
from .api import LoadCSVAPIView

app_name = "api"

urlpatterns = [
    path("load_csv/", LoadCSVAPIView.as_view(), name="load_csv"),
]
