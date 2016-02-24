from rest_framework import serializers
from models import Player, WeekPerformance


class WeekPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekPerformance
        fields = ('week', 'points')

class PlayerSerializer(serializers.ModelSerializer):
    WeekPerformances = WeekPerformanceSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('name', 'position', 'team', 'total_points', 'salary', 'opp', 'fppg', 'WeekPerformances')
