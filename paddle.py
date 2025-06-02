from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.goto(position)
        

    def key_up(self):
        new_yc=self.ycor()+ 20
        self.goto(self.xcor(),new_yc)
    def key_down(self):
        new_yc=self.ycor()- 20
        self.goto(self.xcor(),new_yc)
    
        
