from match import Match, MatchStatus
from team import Team
import event as ev
import random


class MatchEventGenerator:
    @staticmethod
    def play_match(match: Match, host: Team, guest: Team):
        # print(f'Сегодня, на стадионе {match.stadium} состоится {match.number} матч Чемпионата мира по футболу 2022')
        #
        # print(f'В рамках данного матча встречаются команды {host} и {guest}\n')
        # print(f'Стартовый состав команды хозяев {host.name}:')
        # host.first11_presentation()

        # print()
        # print(f'Стартовый состав команды  гостей {guest}:')
        # guest.first11_presentation()

        print(f'Рейтинг команд: {host.name} - {host.get_rating()}   :    {guest.name} - {guest.get_rating()}')
        #print()

        match_time = 0
        second_time = False
        while match_time <= 90:
            match_time += 1
            if random.random() < 0.2:  # chance 10% - scoring moment
                if random.random() < host.get_rating() / (
                        host.get_rating() + guest.get_rating()):  # 55% host_chance - 45% guest_chance .. depends rating
                    team = host
                else:
                    team = guest

                # print(f'CHANCE {team.name}')  # add massages for scoring moment
                match.update_statistics('team, chances + 1')  # here & near add update_statistics method, now its empty

                if random.random() < 0.10:  # 10% goal
                    match_time += 1
                    # ev.goal.print_message(time=str(match_time), team=team.name, player="Raul")
                    match.update_statistics('team, goals + 1')

                elif random.random() < 0.15:  # 15% corner
                    match_time += 1
                    # ev.corner.print_message(time=str(match_time), team=team.name, player="Raul")
                    match.update_statistics('team, corners + 1')
                    if random.random() < 0.15:  # 15% goal after corner
                        # ev.goal.print_message(time=str(match_time), team=team.name, player="Raul")
                        match.update_statistics('team, goals + 1')
                    elif random.random() < 0.30:  # 30% foul in attack after corner
                        # ev.foul.print_message(time=str(match_time), team=team.name, player="Raul")
                        match.update_statistics('team, fouls + 1')
                        if random.random() < 0.20:  # 20% yellow in attack after foul in attack after corner
                            match_time += 1
                            # ev.yellow_card.print_message(time=str(match_time), team=team.name, player="Raul")
                            match.update_statistics('team, yellows + 1')
                            # after yellow_card maybe we need to check player to red_card

                elif random.random() < 0.20:  # 20% foul in attack
                    # ev.foul.print_message(time=str(match_time), team=team.name, player="Raul")
                    match.update_statistics('team, fouls + 1')
                    if random.random() < 0.20:  # 20% yellow in attack after foul in attack after corner
                        match_time += 1
                        # ev.yellow_card.print_message(time=str(match_time), team=team.name, player="Raul")
                        match.update_statistics('team, yellows + 1')
                        # after yellow_card maybe we need to check player to red_card

                elif random.random() < 0.15:  # 15% offside
                    match_time += 1
                    # ev.offside.print_message(time=str(match_time), team=team.name, player="Raul")
                    match.update_statistics('team, offsides + 1')

                elif random.random() < 0.10:  # 10% penalty
                    match_time += 1
                    # ev.penalty.print_message(time=str(match_time), team=team.name, player="Raul")
                    match.update_statistics('team, penalty + 1')
                    if random.random() < 0.75:  # 75% goal after penalty
                        # ev.goal.print_message(time=str(match_time), team=team.name,
                        #                      player="Raul")  # maybe need add special events to goal after penalty
                        match.update_statistics('team, goals + 1')

            if match_time > 45 and second_time is False:
                # ev.second_half.print_message(time=str(match_time))
                second_time = True

            if match_time >= 90:
                match_time += 3
                # ev.full_time.print_message(time=str(match_time))

        return match.statistics