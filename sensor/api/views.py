from rest_framework.generics import CreateAPIView, ListAPIView

from sensor.api.serializers import SensorSerializer


class SensorAPIView(CreateAPIView):
    serializer_class = SensorSerializer


class SensorListAPIView(ListAPIView):
    serializer_class = SensorSerializer
    queryset = SensorSerializer.Meta.model.objects.all()
