import json

from constants import POSITION_CHOICES
from urllib2 import Request, urlopen, URLError
from models import Player, WeekPerformance


def get_player_points(maxweek=1):

    base_url = 'http://api.fantasy.nfl.com/v1/players/stats?statType=weekStats&season=2015&format=json&week='

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



def process_as_dk(pos, draft_kings_stats):
    """
    Returns DK equivalent points
    given stats from NFL API
    """
    points = 0
    if pos != 'DEF':
        points += (int(draft_kings_stats['6']) * 4)
        points += (int(draft_kings_stats['5']) * 0.04)
        if int(draft_kings_stats['5']) >= 300:
            points += 3
        points -= (int(draft_kings_stats['7']) * 1)
        points += (int(draft_kings_stats['14']) * 0.1)
        points += (int(draft_kings_stats['15']) * 6)
        if int(draft_kings_stats['14']) >= 100:
            points += 3
        points += (int(draft_kings_stats['21']) * 0.1)
        points += (int(draft_kings_stats['20']) * 1)
        points += (int(draft_kings_stats['22']) * 6)
        if int(draft_kings_stats['21']) >= 100:
            points += 3
        points += (int(draft_kings_stats['28']) * 6)
        points -= (int(draft_kings_stats['30']) * 1)
        points += (int(draft_kings_stats['32']) * 2)
        points += (int(draft_kings_stats['29']) * 6)
    elif pos == 'DEF':
        points += (int(draft_kings_stats['45']) * 1)
        points += (int(draft_kings_stats['46']) * 2)
        points += (int(draft_kings_stats['47']) * 2)
        points += (int(draft_kings_stats['53']) * 6)
        points += (int(draft_kings_stats['50']) * 6)
        points += (int(draft_kings_stats['49']) * 2)
        points += (int(draft_kings_stats['51']) * 2)

        points_allowed = int(draft_kings_stats['54'])
        if points_allowed == 0:
            points += 10
        elif 1 <= points_allowed <= 6:
            points += 7
        elif 7 <= points_allowed <= 13:
            points += 4
        elif 14 <= points_allowed <= 20:
            points += 1
        elif 28 <= points_allowed <= 34:
            points -= 1
        elif 35 <= points_allowed:
            points -= 4
    else:
        return 0
    return points