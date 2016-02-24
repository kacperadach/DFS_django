import json

from constants import POSITION_CHOICES
from urllib2 import Request, urlopen, URLError
from models import Player, WeekPerformance
from constants import base_url

from PyFL.nfl_stats import process_as_dk


def get_all_player_data(maxweek):
    get_player_points(maxweek)
    fill_player_week_performances(maxweek)
    fill_total_points()

def get_player_points(maxweek=1):
    week = 1
    while(1):
        for position in POSITION_CHOICES:
            url = base_url + str(week) + '&position=' + position[0]
            response = urlopen(Request(url))
            data = json.loads(response.read())
            for player in data['players']:
                p = Player.objects.get_or_create(name=player['name'])[0]
                p.position = player['position']
                p.team = player['teamAbbr']
                p.save()

                draft_kings_stats = {}
                for x in xrange(91):
                    try:
                        num_str = str(x)
                        draft_kings_stats[num_str] = player['stats'][num_str]
                    except KeyError:
                        draft_kings_stats[num_str] = '0'
                try:
                    wp = WeekPerformance.objects.get(player=p, week=week, points=process_as_dk(player['position'], draft_kings_stats))
                except WeekPerformance.DoesNotExist:
                    wp = WeekPerformance.objects.create(player=p, week=week, points=process_as_dk(player['position'], draft_kings_stats))
        week += 1
        if week > maxweek:
            break

def fill_player_week_performances(maxweek=1):
    players = Player.objects.all()
    for player in players:
        for x in range(maxweek):
            week = x+1
            wp = WeekPerformance.objects.filter(player=player, week=week)
            if not wp:
                WeekPerformance.objects.create(player=player, week=week, points=0)

def fill_total_points():
    players = Player.objects.all()
    for player in players:
        wp = WeekPerformance.objects.filter(player=player)
        sum = 0
        for p in wp:
            sum += p.points
        player.total_points = sum
        player.save()

def get_player_salaries():
    # temporarily making salaries 0 to work on frontend
    players = Player.objects.all()
    for player in players:
        player.salary = 0
        player.opp = 'N/A'
        player.fppg = 0
        player.save()




