import json


class Group:
    def __init__(self, name, teams):
        """Constructor"""
        self.name = name
        self.teams = teams


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
