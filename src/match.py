class Match:
    def __init__(self, stadium, date, host, guest, status=False, attendance=None, events=None, statistics=None):
        self.stadium = stadium
        self.date = date
        self.host = host
        self.guest = guest
        self.status = status
        self.attendance = attendance
        self.events = events
        self.statistics = statistics

    def add_event(self, event):
        self.events.append(event)

    def update_statistics(self, statistics):
        self.statistics = statistics

    @staticmethod
    def bad_formation(formation):
        if not isinstance(formation, str) or len(formation.split('-')) != 3 or \
                not all([i.isdigit() for i in (formation.split('-'))]) or sum(map(int, formation.split('-'))) != 10:
            return True

    @staticmethod
    def player_miss_match(player):
        if player.statistics['injured'] or player.statistics['red']:
            return True

    @staticmethod
    def ideal_squad(team, formation='4-4-2'):
        first_11 = []
        goalkeepers, defenders, midfielders, forwards = [], [], [], []
        def_positions = ('LB', 'CB', 'RB', 'LWB', 'RWB')
        mid_positions = ('CDM', 'LM', 'CM', 'RM', 'CAM')
        frw_positions = ('LW', 'RW', 'ST', 'SS')

        if Match.bad_formation(formation):
            formation = '4-4-2'

        def_slots, mid_slots, frw_slots = map(int, formation.split('-'))

        for player in team.players:
            if player.position == 'GK':
                goalkeepers.append(player)
            elif player.position in def_positions and not Match.player_miss_match(player):
                defenders.append(player)
            elif player.position in mid_positions and not Match.player_miss_match(player):
                midfielders.append(player)
            elif player.position in frw_positions and not Match.player_miss_match(player):
                forwards.append(player)

        if def_slots > len(defenders) or mid_slots > len(midfielders) or frw_slots > len(forwards):
            def_slots, mid_slots, frw_slots = 4, 4, 2

        first_11.append(max(goalkeepers))
        defenders.sort(reverse=True)
        for i in range(def_slots):
            first_11.append(defenders[i])
        midfielders.sort(reverse=True)
        for i in range(mid_slots):
            first_11.append(midfielders[i])
        forwards.sort(reverse=True)
        for i in range(frw_slots):
            first_11.append(forwards[i])

        if len(first_11) == 11:
            return first_11, 0
        else:
            bad_positions = 0
            while len(first_11) != 11:
                for player in team.players:
                    if player not in first_11 and not player.statistics['injured'] and not player.statistics['red']:
                        first_11.append(player)
                        bad_positions += 1
            return first_11, bad_positions
