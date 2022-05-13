class Team:
    def __init__(self, name, players, matches=[], flag=None, coach=''):
        self.name = name
        self.flag = flag
        self.players = players
        self.matches = matches
        self.coach = coach

    def add_match(self, match):
        self.matches.append(match)
