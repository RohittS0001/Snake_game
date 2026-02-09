from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game= True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

# Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game = False
        scoreboard.game_over()

# Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        # (bcz we already start from 1 and not 0, so we are not checking the head with itself)
        #     pass
        if snake.head.distance(segment) < 10:
            game = False
            scoreboard.game_over()

screen.exitonclick()