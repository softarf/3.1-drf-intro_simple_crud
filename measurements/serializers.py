from rest_framework import serializers

from measurements.models import Measurement, Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at']    # Отображаемые поля.


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['id', 'project', 'value', 'created_at']    # Отображаемые поля.


class NestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'value', 'created_at']    # Отображаемые поля.


class ProjectDetailSerializer(serializers.ModelSerializer):

    measurements = NestedSerializer(read_only=True, many=True, required=False)  # Maybe optionally measurements.

    class Meta:
        model = Project
        fields = ['id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at', 'measurements']
