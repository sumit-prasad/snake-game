from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.6)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def generate_food(self):
        return randint(-260, 260)

    def refresh(self):
        random_x = self.generate_food()
        random_y = self.generate_food()

        # square = False
        # x_true, y_true = False, False
        #
        # while not square:
        #     if not random_x % 10:
        #         random_x = self.generate_food()
        #     else:
        #         x_true = True
        #     if not random_y % 10:
        #         random_y = self.generate_food()
        #     else:
        #         y_true = True
        #     if x_true and y_true:
        #         square = True

        self.goto(random_x, random_y)

