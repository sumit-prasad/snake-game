from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Helvetica Neue", 12, "bold")


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.print_score()
        self.penup()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.print_score()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.print_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", False, align=ALIGNMENT, font=FONT)

