import csv

from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

from sensor.models import Sensor


class SensorGraphView(ListView):
    queryset = Sensor.objects.all()
    template_name = "sensor_v2.html"


def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sensor_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['start_time', 'end_time', 'time_interval', 'distance'])

    sensors = Sensor.objects.all()
    for sensor in sensors:
        writer.writerow([sensor.start_time, sensor.end_time, sensor.time_interval, sensor.distance])

    return response
