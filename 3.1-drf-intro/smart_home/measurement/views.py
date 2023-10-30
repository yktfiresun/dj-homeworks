from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer,SensorMeasurementSerializer, MeasurementSerializer

class SensorListCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorMeasurementSerializer


class MeasurementCreateAPIView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer