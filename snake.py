import turtle
from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake_len = []
        self.create_snake()
        self.head = self.snake_len[0]
    def create_snake(self):
        add_x = 0
        for i in range(3):
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.setpos(0 - add_x, 0)
            add_x += 20
            self.snake_len.append(snake)
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def move(self):
        for i in range(len(self.snake_len) - 1, 0, -1):
            new_x = self.snake_len[i - 1].xcor()
            new_y = self.snake_len[i - 1].ycor()
            self.snake_len[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


