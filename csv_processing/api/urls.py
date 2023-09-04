from django.urls import path
from .api import LoadCSVAPIView, FavoriteUsersAPIView

app_name = "api"

urlpatterns = [
    path("load_csv/", LoadCSVAPIView.as_view(), name="load_csv"),
    path("favorites/", FavoriteUsersAPIView.as_view(), name="favorites"),
]
