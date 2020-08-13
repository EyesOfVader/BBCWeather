from django.shortcuts import render
from rest_framework import viewsets
from .models import Forecast
from .serializers import ForecastSerializer


class ForecastView(viewsets.ModelViewSet):
    serializer_class = ForecastSerializer
    queryset = Forecast.objects.all()

    def get_queryset(self):
        location = self.request.query_params.get('location', None)
        if location:
            self.queryset = self.queryset.filter(location__name=location)
        return self.queryset

