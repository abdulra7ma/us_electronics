from django.contrib import admin
from django.urls import path, include

from sensor.views import SensorGraphView, download_csv

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("sensor.api.urls")),
    path("graph/", SensorGraphView.as_view(), name="graph"),
    path("data_csv", download_csv, name="data_csv"),
]
