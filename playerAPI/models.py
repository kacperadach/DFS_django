from django.db import models
from constants import *


class Player(models.Model):

    name = models.CharField(
        max_length=100,
        blank=False,
        unique=True,
    )
    position = models.CharField(
        max_length=100,
        choices=POSITION_CHOICES,
    )
    team = models.CharField(
        max_length=100,
        blank=False,
    )

class WeekPerformance(models.Model):

    player = models.ForeignKey(Player)

    week = models.IntegerField(blank=False)
    points = models.IntegerField(blank=False)
