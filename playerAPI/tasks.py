import json

from celery.task import task
from constants import POSITION_CHOICES
from urllib2 import Request, urlopen, URLError
from models import Player, WeekPerformance



#@task
def get_player_points(week=None):

    base_url = 'http://api.fantasy.nfl.com/v1/players/stats?statType=weekStats&season=2015&format=json&week='

    if week is not None:
        pass
    else:
        week = 1
        while(1):
            for position in POSITION_CHOICES:
                url = base_url + str(week) + '&position=' + position[0]
                response = urlopen(Request(url))
                data = json.loads(response.read())
                for player in data['players']:
                    p = Player.objects.get_or_create(name=player['name'])
                    p[0].position = player['position']
                    p[0].team = player['teamAbbr']
                    p[0].save()
                    

