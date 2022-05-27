import match
import stadium
import event
import schedule
import player
import json


class Team:
    def __init__(self, name, players, flag=None, coach=''):
        self.name = name
        self.flag = flag
        self.players = players
        self.coach = coach

    @staticmethod
    def teams_from_json(filename: str):
        data = ''
        with open('../data/players.json') as files:
            text = files.read()
            data = json.loads(text)

        with open('../data/flags.json') as file:
            flags = json.load(file)

        teams = list()
        for team_name in data.keys():
            players = list()
            for player_info in data[team_name]:
                pl = player.Player(**player_info)
                players.append(pl)
                pl.statistics = dict({'injured': False, 'red': False})
            tm = Team(team_name, players, flag=flags[team_name])
            teams.append(tm)
        return teams

    def get_rating(self, m, teams):
        rating = 0
        for team in teams:
            if self.name == team.name:
                first11 = match.Match.ideal_squad(m, team)
                for pl in first11[0]:
                    rating += pl.rating
                rating -= 500
        return rating

    def first11_presentation(self, m, teams):
        for team in teams:
            if self.name == team.name:
                first11 = match.Match.ideal_squad(m, team)
                for pl in first11[0]:
                    print(pl.name, pl.surname, pl.position, pl.rating)
                print()

