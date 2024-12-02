class player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_name(self):
        return self.name    

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score
            
    def add_point(self):
        self.score += 1        