from django.urls import path

from sensor.api.views import SensorAPIView, SensorListAPIView

urlpatterns = [
    path("add_data/", SensorAPIView.as_view(), name="sensor"),
    path("data", SensorListAPIView.as_view(), name="sensor_list"),
]
