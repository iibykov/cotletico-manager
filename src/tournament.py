from match_event_generator import MatchEventGenerator
from schedule import Schedule
from match import Match, MatchStatus


class Tournament:
    def __init__(self, name: str, schedule: Schedule, teams, groups):
        self.name = name
        self.schedule = schedule
        self.teams = teams
        self.groups = groups
        self.generator = MatchEventGenerator()

    def __get_team(self, team_name: str):
        for team in self.teams:
            if team.name == team_name:
                return team
        return None

    def run(self):
        while self.schedule.has_next_match():
            self.play_next_match()

    def play_next_match(self):
        match = self.schedule.get_next_match()
        host = self.__get_team(match.host)
        guest = self.__get_team(match.guest)

        # if unknown team
        if host is not None and guest is not None:
            self.generator.play_match(match, host, guest)
        self.schedule.set_match_status(match.number, MatchStatus.PLAYED)

    def get_winner(self):
        pass
