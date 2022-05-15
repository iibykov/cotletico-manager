import match
import stadium
import event
import schedule


class Team:
    def __init__(self, name, players, flag=None, coach=''):
        self.name = name
        self.flag = flag
        self.players = players
        self.coach = coach
