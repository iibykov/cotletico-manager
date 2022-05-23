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


def groups_from_json(filename: str):
    data = ''
    with open(filename) as files:
        text = files.read()
        data = json.loads(text)

    groups = list()
    for group_name in data.keys():
        group = Group(group_name, data[group_name])
        groups.append(group)


groups_from_json('../data/group.json')

print(Group.team_position('Senegal'))
