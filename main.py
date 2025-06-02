from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time 
from scoreboard import Scoreboard

my_screen=Screen()
my_screen.setup(width=800,height=600)
my_screen.bgcolor("black")
my_screen.title("Ping Pong!")
my_screen.tracer(0)
scoreboard=Scoreboard()


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()

my_screen.listen()
my_screen.onkey(r_paddle.key_up,"Up")
my_screen.onkey(r_paddle.key_down,"Down")
my_screen.onkey(l_paddle.key_up,"w")
my_screen.onkey(l_paddle.key_down,"s")

game_is_on=True
while game_is_on:
    my_screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

# when ball hits the paddle upper and down corner's
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

# when ball hits the paddle's on side corner's
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320 :
        ball.bounce_x()
        
        
# when ball is missed by right paddle
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
# when ball is missed by left paddle
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()

























my_screen.exitonclick()