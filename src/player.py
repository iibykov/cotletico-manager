class Player:
    def __init__(self, name, surname, position, rating, birthdate, number, team, statistics):
        self.name = name
        self.surname = surname
        self.position = position
        self.rating = rating
        self.birthdate = birthdate
        self.number = number
        self.team = team
        self.statistics = statistics

    def update_statistics(self, statistics):
        self.statistics = statistics

    def __lt__(self, other):
        return self.rating < other.rating

    def __add__(self, other):
        return self.rating + self.rating
