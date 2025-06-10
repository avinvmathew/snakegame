import time
from turtle import Screen, Turtle

screen = Screen()
screen.title("The OG snake game")
screen.bgcolor("black")
screen.setup(600,600)
screen.tracer(0)

snake_len = []
is_game_on = True
add_x = 0
for i in range(3):
    snake = Turtle("square")
    snake.penup()
    snake.color("white")
    snake.setpos(0 - add_x,0)
    add_x += 20
    snake_len.append(snake)


while is_game_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(snake_len) - 1, 0, -1):
        new_x = snake_len[i - 1].xcor()
        new_y = snake_len[i - 1].ycor()
        snake_len[i].goto(new_x,new_y)
    snake_len[0].forward(20)
    snake_len[0].left(90)





screen.exitonclick()