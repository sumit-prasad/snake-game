import time
from turtle import Screen
from snake import Snake
from food import Food
from scorecard import Scorecard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Scorecard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extent()
        score.update()

    # Detect collision with wall
    if snake.hit_wall():
        snake.reset_snake()
        score.reset_game()

    # Detect collision with tail
    if snake.hit_tail():
        snake.reset_snake()
        score.reset_game()


screen.exitonclick()
