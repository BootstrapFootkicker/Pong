from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.create_paddle(position)




    def create_paddle(self,position):
        self.shape("square")
        self.color("white")
        self.penup()
        #self.hideturtle()
        self.speed("fastest")
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.goto(position)

    def up(self):
        self.sety(self.ycor()+20)

    def down(self):
        self.sety(self.ycor()-20)

