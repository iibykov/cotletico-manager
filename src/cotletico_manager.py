import random
import json


class Player:
    def __init__(self, name, surname, position, rating, birthdate, number, team, statistics):
        self.name = name
        self.surname = surname
        self.position = position
        self.rating = rating
        self.birthdate = birthdate
        self.number = number
        self.team = team
        self.statistics = statistics

    def update_statistics(self, statistics):
        self.statistics = statistics


class Team:
    def __init__(self, name, players, matches=[], flag=None, coach=''):
        self.name = name
        self.flag = flag
        self.players = players
        self.matches = matches
        self.coach = coach

    def add_match(self, match):
        self.matches.append(match)


class Match:
    def __init__(self, stadium, attendance, date, host, guest, events, statistics):
        self.stadium = stadium
        self.attendance = attendance
        self.date = date
        self.host = host
        self.guest = guest
        self.events = events
        self.statistics = statistics

    def add_event(self, event):
        self.events.append(event)

    def update_statistics(self, statistics):
        self.statistics = statistics


class Stadium:
    def __init__(self, name, city, capacity, image):
        self.name = name
        self.city = city
        self.players = capacity
        self.image = image


class Event:
    def __init__(self, type, time):
        self.type = type
        self.time = time


class Schedule:
    def __init__(self, matches):
        self.matches = matches

    def add_match(self, match):
        self.matches.append(match)


def teams_from_json(filename: str):
    data = ''
    with open('../data/players.json') as files:
        text = files.read()
        data = json.loads(text)

    teams = list()
    for team_name in data.keys():
        players = list()
        for player_info in data[team_name]:
            player = Player(**player_info)
            players.append(player)
        team = Team(team_name, players)
        teams.append(team)
    return teams


teams = teams_from_json('../data/players.json')
print(len(teams))


def ideal_squad(team, formation='4-4-2'):
    first_11 = []
    goalkeepers, defenders, midfielders, forwards = [], [], [], []
    def_positions = ('LB', 'CB', 'RB', 'LWB', 'RWB')
    mid_positions = ('CDM', 'LM', 'CM', 'RM', 'CAM')
    frw_positions = ('LW', 'RW', 'ST', 'SS')

    if not isinstance(formation, str) or len(formation.split('-')) != 3 or \
            not all([i.isdigit() for i in (formation.split('-'))]) or sum(map(int, formation.split('-'))) != 10:
        formation = '4-4-2'
    def_slots, mid_slots, frw_slots = map(int, formation.split('-'))

    for player in team.players:
        if player.position == 'GK':
            goalkeepers.append(player)
        elif player.position in def_positions:
            defenders.append(player)
        elif player.position in mid_positions:
            midfielders.append(player)
        elif player.position in frw_positions:
            forwards.append(player)

    if def_slots > len(defenders) or mid_slots > len(midfielders) or frw_slots > len(forwards):
        def_slots, mid_slots, frw_slots = 4, 4, 2

    first_11.append(max(goalkeepers))
    defenders.sort(reverse=True)
    for i in range(def_slots):
        first_11.append(defenders[i])
    midfielders.sort(reverse=True)
    for i in range(mid_slots):
        first_11.append(midfielders[i])
    forwards.sort(reverse=True)
    for i in range(frw_slots):
        first_11.append(forwards[i])

    return first_11
