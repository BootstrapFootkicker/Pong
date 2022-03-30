from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import  time


screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

scoreboard=Scoreboard()
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball=Ball()

screen.listen()

screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    print(ball.xcor())
    #detect ceiling and floor collision
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect paddle collsion
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()


    #out of bounds
    if ball.xcor()>450:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -450:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()
