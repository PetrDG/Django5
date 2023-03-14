# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerialializer, MeasurementSerialializer, SensorDetailSerializer

class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialializer

class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerialializer

class SensorViewQ(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

