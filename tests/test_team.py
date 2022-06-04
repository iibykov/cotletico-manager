import unittest
from src.team import Team


class TestPlayer(unittest.TestCase):
    def setUp(self):
        """
        Initializing a national team from a text file
        """
        teams = Team.from_json_file('../data/players.json', '../data/flags.json')
        self.team = teams[0]

    def test_get_goalkeepers_all(self):
        self.assertEqual(len(self.team.get_goalkeepers()), 3)

    def test_get_best_goalkeeper(self):
        best_goalkeeper = self.team.get_goalkeepers(None, 1)[0]
        self.assertEqual(best_goalkeeper.rating, 83)  # 'Jordan Pickford' 83

    def test_get_best_forward(self):
        best_forward = self.team.get_forwards(None, 1)[0]
        self.assertEqual(best_forward.rating, 90)  # 'Harry Kane' 90

    def test_ideal_squad(self):
        self.assertEqual(len(self.team.ideal_squad), 11)
        self.assertEqual(self.team.get_rating(), 941)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()
