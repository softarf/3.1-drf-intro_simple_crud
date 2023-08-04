# Использую:
# ListCreateAPIView и RetrieveUpdateDestroyAPIView  для модели  Project
# ListCreateAPIView                                 для модели  Measurement

from rest_framework import generics

from measurements.models import Measurement, Project
from measurements.serializers import MeasurementSerializer, ProjectSerializer, ProjectDetailSerializer


class ProjectAPICreate(generics.ListCreateAPIView):
    """ Создаёт датчик и показывает все. """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    """ Показывает и изменяет датчик.
        "Удаление" по заданию не требуется. Метод 'DELETE' используется только для отладки работоспособности приложения.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    lookup_field = 'name'

    def perform_update(self, serializer):
        """ При переносе датчика в другой город старые замеры удаляются.
        """
        project_name = serializer.instance.name
        Measurement.objects.filter(project__name=project_name).delete()

        serializer.save()


class MeasurementAPICreate(generics.ListCreateAPIView):
    """ Создаёт замер.
        Показывает все замеры - используется только для отладки работоспособности приложения.
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class MeasurementView(generics.RetrieveAPIView):
    """ Показывает один замер - используется только для отладки работоспособности приложения. """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
