from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.color("white")
        self.hideturtle()
        self.player_score = 0
        self.computer_score = 0

    def update_score(self):
        self.goto(-100,200)
        self.write(arg=f"{self.player_score}",align="center", font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(arg=f"{self.computer_score}",align="center", font=("Courier", 80, "normal"))

    def player(self):
        self.player_score += 1
        self.clear()
        self.update_score()

    def computer(self):
        self.computer_score += 1
        self.clear()
        self.update_score()

