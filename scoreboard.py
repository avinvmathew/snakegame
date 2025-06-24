from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0,260)
        self.color("white")
        self.hideturtle()

        with open("highscore.txt","r") as data:
            self.highscore = int(data.read())
        # self.highscore = 0
        self.score = 0
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(arg=f"Your Score {self.score} High Score = {self.highscore}", align = ALIGNMENT, font = FONT)
    def increase_score(self):
        self.score += 1
        self.update_score()
    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt","w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER !", align=ALIGNMENT, font=FONT)


