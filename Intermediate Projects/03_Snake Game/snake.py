from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []

        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)

            self.segments.append(segment)

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()

            self.segments[segment_num].goto(new_x, new_y)

        self.head.forward(MOVING_DISTANCE)

    def snake_grow(self):
        last_segment = self.segments[-1]

        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(last_segment.position())

        self.segments.append(segment)

    def snake_reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)

        self.segments.clear()

        self.create_snake()
        self.head = self.segments[0]

    def tail_collide(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 15:
                return True

        return False

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