from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0,260)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.increase_score()
    def increase_score(self):
        self.clear()
        self.write(arg=f"Your Score {self.score}", align = ALIGNMENT, font = FONT)
        self.score += 1
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER !", align=ALIGNMENT, font=FONT)


