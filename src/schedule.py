import json
import match
import team
import event as ev
import random


class Schedule:
    def __init__(self, matches, teams_matches=0):
        self.matches = matches
        self.teams_matches = teams_matches

    def add_match(self, match):
        self.matches.append(match)

    def get_matches(self, match):
        self.teams_matches.append(match)

    @staticmethod
    def from_json_file(filename: str):
        data = ''
        with open(filename) as files:
            text = files.read()
            data = json.loads(text)

        matches = list()
        for match_info in data:
            m = match.Match(match_info["Match"], match_info["Location"], match_info["Date"], match_info["Team 1"],
                            match_info["Team 2"], [], [])
            matches.append(m)

        schedule = Schedule(matches)
        return schedule

    def get_match(self, number):
        for m in self.matches:
            if m.number == str(number):
                return m

    def play_match(self, number_of_match, teams):
        m = self.get_match(number_of_match)
        host_name, gest_name = m.host, m.guest
        host_rating = 1
        gest_rating = 1
        print(f'Сегодня, на стадионе {m.stadium} состоится {m.number} матч Чемпионата мира по футболу 2022')
        print(f'В рамках данного матча встречаются команды {host_name} и {gest_name}')
        print()
        for t in teams:
            if host_name == t.name:
                host_team = t
                host_rating = t.get_rating(m, teams)
                print(f'Стартовый состав команды хозяев {host_name}:')
                t.first11_presentation(m, teams)
                print()
            if gest_name == t.name:
                gest_team = t
                gest_rating = t.get_rating(m, teams)
                print(f'Стартовый состав команды  гостей {gest_name}:')
                t.first11_presentation(m, teams)

        print(f'рейтинг команд: {host_name} - {host_rating}   :    {gest_name} - {gest_rating}')
        print()

        chance = ev.ChanceState()
        goal = ev.GoalState()
        reject_goal = ev.RejectGoalState()
        corner = ev.CornerState()
        foul = ev.FoulState()
        yellow = ev.YellowState()

        host_event = ev.Event(chance)
        gest_event = ev.Event(chance)

        match_time = 0
        while match_time < 90:
            match_time += 1
            if random.random() < 0.2:  # chance 20% - scoring moment
                if random.random() < host_rating / (
                        host_rating + gest_rating):  # 55% host_chance - 45% guest_chance ... depends rating
                    team_event = host_event
                    team = host_team
                else:
                    team_event = gest_event
                    team = gest_team

                team_event.change_state(chance)
                print(f'{match_time} минута матча', end=' ')
                print(team.name, end=' ')
                m.update_statistics('team chances + 1')
                team_event.event_action()
                print()

                if random.random() < 0.10:
                    match_time += 1
                    team_event.change_state(goal)
                    print(f'{match_time} минута матча', end=' ')
                    print(team.name, end=' ')
                    m.update_statistics('team chances + 1')
                    team_event.event_action()
                    print()
                    if random.random() < 0.15:
                        team_event.change_state(reject_goal)
                        match_time += 2
                        print(f'{match_time} минута матча', end=' ')
                        print(team.name, end=' ')
                        m.update_statistics('team chances + 1')
                        team_event.event_action()
                        print()
                    continue

                elif random.random() < 0.15:
                    team_event.change_state(corner)
                    print(f'{match_time} минута матча', end=' ')
                    print(team.name, end=' ')
                    m.update_statistics('team corners + 1')
                    team_event.event_action()
                    print()
                    if random.random() < 0.18:
                        match_time += 1
                        team_event.change_state(goal)
                        print(f'{match_time} минута матча', end=' ')
                        print(team.name, end=' ')
                        m.update_statistics('team goals + 1')
                        team_event.event_action()
                        print()
                    elif random.random() < 0.40:
                        match_time += 1
                        team_event.change_state(foul)
                        print(f'{match_time} минута матча', end=' ')
                        print(team.name, end=' ')
                        m.update_statistics('foul + 1')
                        team_event.event_action()
                        print()
                        if random.random() < 0.30:
                            match_time += 1
                            team_event.change_state(yellow)
                            print(f'{match_time} минута матча', end=' ')
                            print(team.name, end=' ')
                            m.update_statistics('yellow + 1')
                            team_event.event_action()
                            print()
                    continue

                elif random.random() < 0.20:
                    match_time += 1
                    team_event.change_state(foul)
                    print(f'{match_time} минута матча', end=' ')
                    print(team.name, end=' ')
                    m.update_statistics('fouls + 1')
                    team_event.event_action()
                    print()
                    if random.random() < 0.30:
                        match_time += 1
                        team_event.change_state(yellow)
                        print(f'{match_time} минута матча', end=' ')
                        print(team.name, end=' ')
                        m.update_statistics('yellow + 1')
                        team_event.event_action()
                        print()
        return m.statistics
