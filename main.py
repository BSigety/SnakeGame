from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# sets up screen for game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()  # creates a new snake object
food = Food()  # creates a new food object
scoreboard = ScoreBoard()  # creates a new scoreboard object

# binds arrow keys to snake object motion
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


snake_is_alive = True
while snake_is_alive:
    # makes it so all snake parts appears to move as one
    screen.update()
    time.sleep(0.15)

    # keeps snake continuously moving
    snake.move()

    # if snake come in contact with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    # checks to see if snake hit any walls
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.game_over()
        snake_is_alive = False

    # checks if snake head has hit any part of the snake body
    for part in snake.snake_body:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 15:
            scoreboard.game_over()
            snake_is_alive = False

screen.exitonclick()
