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

        match_time = 0
        second_time = False
        while match_time <= 90:
            match_time += 1
            if random.random() < 0.2:        #chance 10% - scoring moment
                if random.random() < host_rating / (host_rating + gest_rating):           #55% host_chance - 45% guest_chance ... depends rating
                    team = host_team
                else:
                    team = gest_team
                print(f'CHANCE {team.name}')                 # add massages for scoring moment
                m.update_statistics('team, chances + 1')     # here and near add update_statistics method, now its empty

                if random.random() < 0.10:                   # 10% goal
                    match_time += 1
                    ev.goal.print_message(time=str(match_time), team=team.name, player="Raul")
                    m.update_statistics('team, goals + 1')

                elif random.random() < 0.15:                 # 15% corner
                    match_time += 1
                    ev.corner.print_message(time=str(match_time), team=team.name, player="Raul")
                    m.update_statistics('team, corners + 1')
                    if random.random() < 0.15:               # 15% goal after corner
                        ev.goal.print_message(time=str(match_time), team=team.name, player="Raul")
                        m.update_statistics('team, goals + 1')
                    elif random.random() < 0.30:             # 30% foul in attack after corner
                        ev.foul.print_message(time=str(match_time), team=team.name, player="Raul")
                        m.update_statistics('team, fouls + 1')
                        if random.random() < 0.20:          # 20% yellow in attack after foul in attack after corner
                            match_time += 1
                            ev.yellow_card.print_message(time=str(match_time), team=team.name, player="Raul")
                            m.update_statistics('team, yellows + 1')
                            # after yellow_card maybe we need to check player to red_card

                elif random.random() < 0.20:                # 20% foul in attack
                    ev.foul.print_message(time=str(match_time), team=team.name, player="Raul")
                    m.update_statistics('team, fouls + 1')
                    if random.random() < 0.20:          # 20% yellow in attack after foul in attack after corner
                        match_time += 1
                        ev.yellow_card.print_message(time=str(match_time), team=team.name, player="Raul")
                        m.update_statistics('team, yellows + 1')
                        # after yellow_card maybe we need to check player to red_card

                elif random.random() < 0.15:                # 15% offside
                    match_time += 1
                    ev.offside.print_message(time=str(match_time), team=team.name, player="Raul")
                    m.update_statistics('team, offsides + 1')

                elif random.random() < 0.10:                # 10% penalty
                    match_time += 1
                    ev.penalty.print_message(time=str(match_time), team=team.name, player="Raul")
                    m.update_statistics('team, penalty + 1')
                    if random.random() < 0.75:               # 75% goal after penalty
                        ev.goal.print_message(time=str(match_time), team=team.name, player="Raul")  # maybe need add special events to goal after penalty
                        m.update_statistics('team, goals + 1')

            if match_time > 45 and second_time is False:
                ev.second_half.print_message(time=str(match_time))
                second_time = True

            if match_time >= 90:
                match_time += 3
                ev.full_time.print_message(time=str(match_time))

        return m.statistics
