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

    player = models.ForeignKey(Player, related_name='WeekPerformances')

    week = models.IntegerField(blank=True)
    points = models.IntegerField(blank=True)

    class Meta(object):
        ordering = ['week']

    def __unicode__(self):
        return '{}: {}'.format(self.week, self.points)