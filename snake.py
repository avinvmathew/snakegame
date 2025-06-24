import turtle
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake_len = []
        self.add_x = 0
        self.create_snake()
        self.head = self.snake_len[0]

    def create_snake(self):
        for i in range(3):
            self.add_snake()
    def add_snake(self):
        snake = Turtle("square")
        # snake.hideturtle()
        snake.penup()
        snake.color("blue")
        snake.setpos(0 - self.add_x, 0)
        # snake.showturtle()
        self.add_x += 20
        self.snake_len.append(snake)
    def extend_snake(self):
        self.add_snake()
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def move(self):
        for i in range(len(self.snake_len) - 1, 0, -1):
            new_x = self.snake_len[i - 1].xcor()
            new_y = self.snake_len[i - 1].ycor()
            self.snake_len[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def reset_body(self):
        for seg in self.snake_len:
            seg.goto(1000,1000)
        self.snake_len.clear()
        self.create_snake()
        self.head = self.snake_len[0]



