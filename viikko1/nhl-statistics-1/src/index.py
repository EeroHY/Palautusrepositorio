from statistics_service import StatisticsService, SortBy
from player_reader import PlayerReader

def main():
    stats = StatisticsService(
      PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt")
    )
    
    # järjestetään kaikkien tehopisteiden eli maalit+syötöt perusteella
    print("Top point getters:")
    for player in stats.top(3, SortBy.POINTS):
        print(player)

    # metodi toimii samalla tavalla kuin yo. kutsu myös ilman toista parametria
    for player in stats.top(3):
        print(player)

    # järjestetään maalien perusteella
    print("Top point goal scorers:")
    for player in stats.top(3, SortBy.GOALS):
        print(player)

    # järjestetään syöttöjen perusteella
    print("Top by assists:")
    for player in stats.top(3, SortBy.ASSISTS):
        print(player)
