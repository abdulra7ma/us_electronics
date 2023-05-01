from rest_framework.generics import CreateAPIView, ListAPIView

from sensor.api.serializers import SensorSerializer
from sensor.models import Sensor


class SensorAPIView(CreateAPIView):
    serializer_class = SensorSerializer


class SensorListAPIView(ListAPIView):
    serializer_class = SensorSerializer
    # latest 100 sensors data added to the database
    queryset = Sensor.objects.all().order_by('-end_time')[:100]

