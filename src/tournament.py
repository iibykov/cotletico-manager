from team import Team
from schedule import Schedule

group_schedule = Schedule.from_json_file('../data/schedule.json')
teams = Team.from_json_file('../data/players.json')


class Tournament:
    @staticmethod
    def run():
        """generates all matches in turn"""
        print('Do you want to play a match?')
        answer = input("Please enter 'Yes' or 'No': ")
        print()
        match_number = 1
        if answer != 'Yes' and answer != 'No':
            while answer != 'Yes' and answer != 'No':
                print('Please enter "Yes" or "No" with a capital letter!')
                answer = input('Yes or No: ')
                print()
        if answer == 'No':
            print("Well, let's play another time!")
        while answer == 'Yes':
            print(group_schedule.play_match(match_number, teams), '\n')
            match_number += 1
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

    def play_next_match(self):
        pass

    def get_winner(self):
        pass


Tournament.run()
