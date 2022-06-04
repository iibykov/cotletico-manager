from enum import Enum
from src.team import Team


class MatchStatus(Enum):
    NOT_PLAYED = 0
    PLAYED = 1


class Match:
    def __init__(self, number, stadium, date, host: Team, guest: Team, status=MatchStatus.NOT_PLAYED,
                 attendance=None, events=None, statistics=None):
        self.number = number
        self.stadium = stadium
        self.date = date
        self.host = host
        self.guest = guest
        self.status = status
        self.attendance = attendance
        self.events = events
        self.statistics = statistics

    def add_event(self, event):
        self.events.append(event)

    def update_statistics(self, statistics):
        self.statistics = statistics
