
from turtle import Turtle

MOVE_DIST = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.penup()
        self.x_move = MOVE_DIST
        self.y_move = MOVE_DIST
        self.reset()


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)



    def bounce(self,x_bounce, y_bounce):
        if x_bounce:
            self.x_move*=-1

        if y_bounce:
            self.y_move*= -1

    def reset(self):
        # ball should go to initial position
        # always moving up
        self.goto(x=0,y=-280)
        self.y_move=10