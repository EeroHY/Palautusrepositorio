import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        self.assertEqual(self.stats.search("Semenko").name, "Semenko") 

    def test_search_with_wrong_name(self):
        self.assertEqual(self.stats.search("Selanne"), None) 

    def test_team(self):
        self.assertEqual(self.stats.team("EDM")[0].name, "Semenko")     

    def test_top(self):
        self.assertEqual(self.stats.top(1)[0].name, "Gretzky")     

    def test_top_goals(self):
        self.assertEqual(self.stats.top(1, SortBy.GOALS)[0].name, "Lemieux")         

    def test_top_assists(self):
        self.assertEqual(self.stats.top(1, SortBy.ASSISTS)[0].name, "Gretzky")        