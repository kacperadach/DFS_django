from rest_framework import serializers
from models import Player


class PlayerSerializer(serializers.ModelSerializer):
    WeekPerformances = serializers.StringRelatedField(many=True)

    class Meta:
        model = Player
        fields = ('name', 'position', 'team', 'total_points', 'WeekPerformances')
