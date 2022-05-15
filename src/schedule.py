class Schedule:
    def __init__(self, matches, teams_matches):
        self.matches = matches
        self.teams_matches = teams_matches

    def add_match(self, match):
        self.matches.append(match)

    def get_matches(self, match):
        self.teams_matches.append(match)
