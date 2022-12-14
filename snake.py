from turtle import Turtle

# constants for Snake class
STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):  # initializes snake
        self.snake_body = []
        self.create_new_snake()
        self.head = self.snake_body[0]

    def create_new_snake(self):  # creates starting snake
        for i in range(0, 3):
            body = Turtle('square')
            body.color('white')
            body.penup()
            body.setposition(STARTING_POSITIONS[i], 0)
            self.snake_body.append(body)

    def move(self):  # moves snake in one continuous motion
        for part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[part - 1].xcor()
            new_y = self.snake_body[part - 1].ycor()
            self.snake_body[part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):  # makes snake turn right
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):  # makes snake turn up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):  # makes snake turn left
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):  # makes snake turn down
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def grow(self):
        # creates new body part with all relevant criteria
        new_part = Turtle('square')
        new_part.color('white')
        new_part.penup()

        # adds new snake part to body
        self.snake_body.append(new_part)

