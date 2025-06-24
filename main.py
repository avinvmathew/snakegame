# import turtle
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.title("The OG snake game")
screen.bgcolor("green")
screen.setup(600,600)
#screen.screensize(600,600)
screen.tracer(0)

our_snake = Snake()
food = Food()
score = Scoreboard()
is_game_on = True

screen.listen()
screen.onkey(our_snake.up,"Up")
screen.onkey(our_snake.down,"Down")
screen.onkey(our_snake.right,"Right")
screen.onkey(our_snake.left,"Left")

while is_game_on:
    time.sleep(0.1)
    our_snake.move()
    screen.update()
    #Collisiion detection of snake and food
    dist = our_snake.head.distance(food)
    if dist < 15:
        food.next_location()
        our_snake.extend_snake()
        score.increase_score()
    #collisiom detection of snake and wall
    if  our_snake.head.xcor() > 280 or our_snake.head.ycor() > 280 or our_snake.head.xcor() < -280 or our_snake.head.ycor() < -280:
        #print("Game over")
        # is_game_on = False
        # score.game_over()
        score.reset_scoreboard()
        our_snake.reset_body()
    #detect collision with tail
    for segment in our_snake.snake_len[1: ]:
        if our_snake.head.distance(segment) < 10:
            # is_game_on = False
            # score.game_over()
            score.reset_scoreboard()
            our_snake.reset_body()







screen.exitonclick()