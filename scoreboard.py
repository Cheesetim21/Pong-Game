from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = [0, 0]
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.ht()
        self.update()

    def update(self):
        self.write(f"Score: {self.score[0]} - {self.score[1]}", False, "center", ('Courier', 16, 'normal'))

    def increase_score(self, player):
        if player == 'player':
            self.score[0] += 1
        elif player == 'enemy':
            self.score[1] += 1
        self.clear()
        self.update()

    def game_win(self):
        self.goto(0, 0)
        self.write("You Win", False, "center", ('Courier', 30, 'normal'))

    def game_lose(self):
        self.goto(0, 0)
        self.write("You Lose", False, "center", ('Courier', 30, 'normal'))

    def p_one_win(self):
        self.goto(0, 0)
        self.write("P1 Wins", False, "center", ('Courier', 30, 'normal'))

    def p_two_win(self):
        self.goto(0, 0)
        self.write("P2 Wins", False, "center", ('Courier', 30, 'normal'))