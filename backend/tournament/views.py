from django_filters.rest_framework import DjangoFilterBackend  # Help filter the records
from rest_framework import viewsets, filters

from .models import Tournament, City, Sport, Level
from .serializers import (
    TournamentSerializer,
    SportSerializer,
    CitySerializer,
    LevelSerializer,
)


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ("title", "sport", "city", "level")
    search_fields = "title"
    ordering_fields = ("created_at", "modified_at")


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
