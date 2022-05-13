class Match:
    def __init__(self, stadium, attendance, date, host, guest, events, statistics):
        self.stadium = stadium
        self.attendance = attendance
        self.date = date
        self.host = host
        self.guest = guest
        self.events = events
        self.statistics = statistics

    def add_event(self, event):
        self.events.append(event)

    def update_statistics(self, statistics):
        self.statistics = statistics
