from rest_framework import serializers

# TODO: опишите необходимые сериализаторы

from .models import Sensor, Measurement

class SensorSerialializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', ]

class MeasurementSerialializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']

class MeasurementSerialializerQ(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerialializerQ(many=True, read_only=True,)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements', ]