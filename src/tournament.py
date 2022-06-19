from match_event_generator import MatchEventGenerator
from schedule import Schedule
from match import Match, MatchStatus
from team import Team
from random import randrange


class Tournament:
    def __init__(self, name: str, schedule: Schedule, teams, groups):
        self.name = name
        self.schedule = schedule
        self.teams = teams
        self.groups = groups
        self.generator = MatchEventGenerator()

    def __get_team(self, team_name: str) -> Team:
        for team in self.teams:
            if team.name == team_name:
                return team
        return None

    def get_team_stats(self, team_name: str):
        return self.__get_team(team_name).statistics

    def get_team_names(self, group_name):
        return self.groups.get(group_name)

    def get_teams(self, group_name):
        team_names = self.get_team_names(group_name)
        teams = []
        for team_name in team_names:
            teams.append(self.__get_team(team_name))
        return teams

    def run(self):
        # Play a group round
        while self.schedule.has_next_match():
            self.play_next_match()

        # Determine the arrangement of places in groups
        for group_name in self.groups:
            teams = self.get_teams(group_name)
            teams.sort(key=lambda t: t.statistics, reverse=True)
            print(*teams, sep='\n')

    def play_next_match(self):
        match = self.schedule.get_next_match()
        host = self.__get_team(match.host)
        guest = self.__get_team(match.guest)

        # if unknown team
        if host is not None and guest is not None:
            self.generator.play_match(match, host, guest)

            host_goals, guest_goals = randrange(5), randrange(5)

            if host_goals == guest_goals:
                host.statistics.points += 1
                guest.statistics.points += 1
            elif host_goals > guest_goals:
                host.statistics.points += 3
            else:
                guest.statistics.points += 3

            host.statistics.goals_for = host_goals
            host.statistics.goals_against = guest_goals

            guest.statistics.goals_for = guest_goals
            guest.statistics.goals_against = host_goals

        self.schedule.set_match_status(match.number, MatchStatus.PLAYED)

    def get_winner(self):
        pass
