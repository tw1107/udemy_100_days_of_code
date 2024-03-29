from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# TODO 1: Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# TODO 2: Create and move a paddle
# TODO 3: Create another paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# TODO 4: Create the ball and make it move
ball = Ball()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # TODO 5: Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO 6: Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # TODO 7: Detect when misses
    # when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        # TODO 8: Keep score
        scoreboard.l_point()

    # when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        # TODO 8: Keep score
        scoreboard.r_point()



screen.exitonclick()