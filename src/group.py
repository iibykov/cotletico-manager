import json
import team_position


class Group:
    def __init__(self, name, teams):
        """Constructor"""
        self.name = name
        self.teams = teams

    @staticmethod
    def team_position(team_name):
        """shows the team's current position in the group"""
        return team_position.update_status(team_position.group_name(team_name))

    @staticmethod
    def from_json(data):
        groups = list()
        for group_name in data.keys():
            group = Group(group_name, data[group_name])
            groups.append(group)
        return groups

    @staticmethod
    def from_json_file(filename: str):
        data = ''
        with open(filename) as files:
            text = files.read()
            data = json.loads(text)
        return data
