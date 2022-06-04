from team import Team
from schedule import Schedule

group_schedule = Schedule.from_json_file('../data/schedule.json')
teams = Team.from_json_file('../data/players.json')


class Tournament:
    __matches_played = 0
    __match_number = 1

    @staticmethod
    def run():
        """generates all matches in turn"""
        print('Do you want to play a match?')
        answer = input("Please enter 'Yes' or 'No': ")
        print()

        if answer != 'Yes' and answer != 'No':
            while answer != 'Yes' and answer != 'No':
                print('Please enter "Yes" or "No" with a capital letter!')
                answer = input('Yes or No: ')
                print()
        if answer == 'No':
            print("Well, let's play another time!")
        while answer == 'Yes':
            print(group_schedule.play_match(Tournament.__match_number, teams), '\n')
            Tournament.__match_number += 1
            Tournament.__matches_played += 1
            print('Do you want to play the next match?')
            answer = input('Yes or No: ')
            print()
            if answer != 'Yes' and answer != 'No':
                while answer != 'Yes' and answer != 'No':
                    print('Please enter "Yes" or "No" with a capital letter!')
                    answer = input('Yes or No: ')
                    print()
            if answer == 'No':
                print("Well, let's play another time!")

    @classmethod
    def next_unplayed_match(cls):
        """displays information about the next unplayed match"""
        gsm = group_schedule.matches[cls.__matches_played]
        return f'The next match of the 2022 FIFA World Cup number {gsm.number} ' \
               f'will be held between the {gsm.host} and {gsm.guest} teams ' \
               f'and will take place on {gsm.date} at the {gsm.stadium}!'

    @staticmethod
    def play_next_match():
        Tournament.__matches_played += 1
        return group_schedule.play_match(Tournament.__match_number, teams)

    def get_winner(self):
        pass


Tournament.run()
print()
Tournament.play_next_match()
print()
print(Tournament.next_unplayed_match())
