from enum import Enum


class PlayerStatus(Enum):
    OK = 0
    INJURED = 1
    RED_CARD = 2


class Player:
    def __init__(self, name, surname, position, rating, birthdate, number, team, status=PlayerStatus.OK, statistics=[]):
        self.name = name
        self.surname = surname
        self.position = position
        self.rating = rating
        self.birthdate = birthdate
        self.number = number
        self.team = team
        self.status = status
        self.statistics = statistics

    def __str__(self):
        return f'Player({self.name}, {self.surname}, {self.position}, {self.rating}, {self.birthdate}, {self.number},' \
               f'{self.team}, {self.status}, {self.statistics})'

    def update_statistics(self, statistics):
        self.statistics = statistics

    def __lt__(self, other):
        return self.rating < other.rating

    def can_play(self):
        return self.status == PlayerStatus.OK
