from turtle import Turtle
import random as r

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("red")
        self.speed("fastest")
        self.next_location()
    def next_location(self):
        random_x = r.randint(-280, 280)
        random_y = r.randint(-280, 280)
        self.goto(random_x, random_y)