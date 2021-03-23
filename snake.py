from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]
        self.head.shape("triangle")

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_block(position)

    def add_block(self, position):
        new_block = Turtle(shape="square")
        new_block.shapesize(0.6)
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        self.blocks.append(new_block)

    def extent(self):
        self.add_block(self.blocks[-1].position())

    def move(self):
        for block_no in range(len(self.blocks) - 1, 0, -1):
            x_cor = self.blocks[block_no - 1].xcor()
            y_cor = self.blocks[block_no - 1].ycor()
            self.blocks[block_no].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def clear(self):
        for block in self.blocks:
            block.reset()
        self.__init__()
        return True

    def hit_wall(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290 \
                or self.head.ycor() > 290 or self.head.ycor() < -290:
            return True
        return False

    def hit_tail(self):
        for block in self.blocks[1:]:
            if self.head.distance(block) < 5:
                return True

        return False

    def reset_snake(self):
        for block in self.blocks:
            block.goto(1000, 1000)
        self.blocks.clear()
        self.create_snake()
        self.head = self.blocks[0]
        self.head.shape("triangle")
