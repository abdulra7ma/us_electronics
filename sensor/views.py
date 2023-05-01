from django.views.generic import ListView

from sensor.models import Sensor


class SensorGraphView(ListView):
    queryset = Sensor.objects.all()
    template_name = "sensor_v2.html"
