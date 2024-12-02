from player import player

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player(player1_name)
        self.player2 = player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.get_name():
            self.player1.add_point()
        else:
            self.player2.add_point()

    def get_score(self):

        if self.player1.get_score() == self.player2.get_score():
            if self.player1.get_score() == 0:
                return "Love-All"
            elif self.player1.get_score() == 1:
                return "Fifteen-All"
            elif self.player1.get_score() == 2:
                return "Thirty-All"
            else:
                return "Deuce"

        elif self.player1.get_score()  >= 4 or self.player2.get_score()  >= 4:
            minus_result = self.player1.get_score()  - self. player2.get_score() 

            if minus_result == 1:
                return "Advantage player1"
            elif minus_result == -1:
                return "Advantage player2"
            elif minus_result >= 2:
                return "Win for player1"
            else:
                return "Win for player2"

        else:
            score = ""
            temp_score = 0
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1.get_score() 
                else:
                    score = score + "-"
                    temp_score = self.player2.get_score() 

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"
            return score
