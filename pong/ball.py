from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slow")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed=0.1

    def move(self):
        self.new_x = self.xcor() + self.x_move
        self.new_y = self.ycor() + self.y_move
        self.goto(self.new_x, self.new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        #makes decimal smaller but doesnt go negative.
        self.move_speed*=0.9

    def reset(self):

        self.goto(0, 0)
        self.move_speed=0.1
        self.bounce_x()


    # self.y_move = self.y_move * -1

    def increase_speed(self):
        self.x_move +=10
        self.y_move+=10
