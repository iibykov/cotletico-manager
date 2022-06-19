
class TeamStatistics:
    def __init__(self, points=0, goals_for=0, goals_against=0):
        self.points = points
        self.goals_for = goals_for
        self.goals_against = goals_against

    def __gt__(self, other):
        """
        Comparison of statistics of two teams in all matches.
        Fair play points and statistics scored with teams in question do not count

        Parameters
        ----------
        other: TeamStatistics
            Second team stats.
        """
        # Points obtained in all group matches
        if self.points != other.points:
            return self.points > other.points

        # Goal difference in all group matches
        self_goal_diff = self.goals_for - self.goals_against
        other_goal_diff = other.goals_for - other.goals_against
        if self_goal_diff != other_goal_diff:
            return self_goal_diff > other_goal_diff

        # Number of goals scored in all group matches
        if self.goals_for != other.goals_for:
            return self.goals_for > other.goals_for


class MatchStatistics:
    def __init__(self):
        self.team_host = ""
        self.team_guest = ""

        self.host_goals = 0
        self.guest_goals = 0

        self.host_yellow_cards = 0
        self.guest_yellow_cards = 0

        self.host_red_cards = 0
        self.guest_red_cards = 0


class PlayerStatistics:
    def __init__(self):
        self.goals = 0
        self.assists = 0
        self.yellow_cards = 0
        self.red_cards = 0
