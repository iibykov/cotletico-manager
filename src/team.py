from src.player import PlayerStatus, Player
import json


class Team:
    def __init__(self, name, players, formation='4-4-2', flag=None, coach=''):
        self.name = name
        self.flag = flag
        self.players = players
        self.formation = Team.__check_formation(formation)
        self.coach = coach

    @staticmethod
    def __check_formation(formation: str) -> str:
        default_formation = '4-4-2'
        if not isinstance(formation, str) or len(formation.split('-')) != 3 or \
                not all([i.isdigit() for i in (formation.split('-'))]) or sum(map(int, formation.split('-'))) != 10:
            return default_formation
        return formation

    @staticmethod
    def from_json(data, flags):
        teams = list()
        for team_name in data.keys():
            players = list()
            for player_info in data[team_name]:
                pl = Player(**player_info)
                players.append(pl)
                pl.statistics = dict({'injured': False, 'red': False})
            tm = Team(team_name, players, flag=flags[team_name])
            teams.append(tm)
        return teams

    @staticmethod
    def from_json_file(players_filename: str, flags_filename: str):
        data = ''
        with open(players_filename) as files:
            text = files.read()
            data = json.loads(text)

        with open(flags_filename) as file:
            flags = json.load(file)

        return Team.from_json(data, flags)

    def get_rating(self):
        first11 = self.ideal_squad()
        return sum(pl.rating for pl in first11)

    def get_players_by_position(self, positions, status: PlayerStatus = None, number: int = None):
        players = []
        for player in self.players:
            if player.position in positions:
                players.append(player)
        if status is not None:
            players = filter(lambda pl: pl.status == status, players)
        if number is not None:
            players = sorted(players, reverse=True)[:number]
        return players

    def get_defenders(self, status: PlayerStatus = None, number: int = None):
        return self.get_players_by_position(('LB', 'CB', 'RB', 'LWB', 'RWB'), status, number)

    def get_goalkeepers(self, status: PlayerStatus = None, number: int = None):
        return self.get_players_by_position(('GK',), status, number)

    def get_forwards(self, status: PlayerStatus = None, number: int = None):
        return self.get_players_by_position(('LW', 'RW', 'ST', 'SS'), status, number)

    def get_midfielders(self, status: PlayerStatus = None, number: int = None):
        return self.get_players_by_position(('CDM', 'LM', 'CM', 'RM', 'CAM'), status, number)

    @property
    def ideal_squad(self):
        def_slots, mid_slots, frw_slots = map(int, self.formation.split('-'))

        goalkeepers = self.get_goalkeepers(PlayerStatus.OK, 1)
        defenders = self.get_defenders(PlayerStatus.OK, def_slots)
        midfielders = self.get_midfielders(PlayerStatus.OK, mid_slots)
        forwards = self.get_forwards(PlayerStatus.OK, frw_slots)

        first_11 = goalkeepers + defenders + midfielders + forwards
        return first_11
