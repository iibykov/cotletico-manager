from team import Team
from group import Group
from schedule import Schedule
from tournament import Tournament


def main():
    groups = Group.from_json_file('../data/group.json')
    group_schedule = Schedule.from_json_file('../data/schedule.json')
    teams = Team.from_json_file('../data/players.json', '../data/flags.json')

    world_cup_2022 = Tournament('FIFA World Cup Qatar 2022', group_schedule, teams, groups)
    # print(world_cup_2022.get_team_names("A"))
    world_cup_2022.run()


if __name__ == "__main__":
    main()
