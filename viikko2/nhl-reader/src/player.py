class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.games = dict['games']
        self.id = dict['id']
    def __str__(self):
        return self.name + " team " + self.team + " goals " + self.goals
