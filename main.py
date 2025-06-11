# import turtle
import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.title("The OG snake game")
screen.bgcolor("black")
screen.setup(600,600)
screen.tracer(0)

our_snake = Snake()
is_game_on = True

screen.listen()
screen.onkey(our_snake.up,"Up")
screen.onkey(our_snake.down,"Down")
screen.onkey(our_snake.right,"Right")
screen.onkey(our_snake.left,"Left")

# turtle.onkeypress(key="w", fun=our_snake.turn_left)

while is_game_on:
    screen.update()
    time.sleep(0.2)
    our_snake.move()





screen.exitonclick()