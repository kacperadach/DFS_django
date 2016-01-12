from models import Player
from rest_framework import viewsets
from serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('name')
    serializer_class = PlayerSerializer

class QuarterBackViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.filter(position='QB').order_by('name')
    serializer_class = PlayerSerializer

class RunningBackViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.filter(position='RB').order_by('name')
    serializer_class = PlayerSerializer

class WideReceiverViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.filter(position='WR').order_by('name')
    serializer_class = PlayerSerializer

class TightEndViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.filter(position='TE').order_by('name')
    serializer_class = PlayerSerializer

class DefenseViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.filter(position='DEF').order_by('name')
    serializer_class = PlayerSerializer
