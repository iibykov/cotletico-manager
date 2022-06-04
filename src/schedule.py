import json
from match import Match, MatchStatus
import team


class Schedule:
    def __init__(self, matches):
        self.matches = matches

    def get_next_match(self) -> Match:
        return next((match for match in self.matches if match.status == MatchStatus.NOT_PLAYED), None)

    def has_next_match(self) -> bool:
        return self.get_next_match() is not None

    def add_match(self, match):
        self.matches.append(match)

    @staticmethod
    def from_json(data):
        matches = list()
        for match_info in data:
            m = Match(match_info["Match"], match_info["Location"], match_info["Date"], match_info["Team 1"],
                      match_info["Team 2"], status=MatchStatus.NOT_PLAYED)
            matches.append(m)

        schedule = Schedule(matches)
        return schedule

    @staticmethod
    def from_json_file(filename: str):
        data = ''
        with open(filename) as files:
            data = json.loads(files.read())
        return Schedule.from_json(data)

    def get_match(self, number):
        return filter(lambda m: m.number == number, self.matches)

    def set_match_status(self, number, status: MatchStatus):
        for i in range(len(self.matches)):
            if self.matches[i].number == number:
                self.matches[i].status = status
                break
