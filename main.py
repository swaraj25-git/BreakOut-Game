

import turtle as tr
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import ScoreBoard
from ui import Ui
import time


# print('Hello')

"""
For breakoit game
using turtle
create a window/ screen
bottom screen a horizontal brick
it should be moved by pressing left right keys
a ball
and bricks at top part of screen
ball will hit the baricks at top part
bouncce back and using ledt/right keys move the bottom brick /paddle
ball wil hit the padle and again bounce back

"""

#####Structure

###
# ball.py
# main.py
# bricks.py
# ui.py
# paddle.py
#scoreboard.py
# ###



####    Main code start Here👇    ###

# a turtle window with black bg

win  = tr.Screen()
win.setup(width=1200, height=600)
win.bgcolor('Black')
win.title('BreakOut!')
win.tracer(0)


ui = Ui()
ui.header()

score = ScoreBoard(lives=5)
paddle = Paddle()
ball = Ball()
bricks = Bricks()

playing_game = True
game_paused = False

def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True


win.listen()
win.onkey(key='Left',fun=paddle.move_left)
win.onkey(key='Right',fun=paddle.move_right)
win.onkey(key='space',fun=pause_game)

def check_collision_with_walls():
    global ball, score, playing_game, ui

    if ball.xcor() < -580 or ball.xcor() >570:
        ball.bounce(x_bounce=True, y_bounce=False)
        return

    if ball.ycor() > 270:
        ball.bounce(x_bounce=False, y_bounce=True)
        return

    if ball.ycor() < -280:
        ball.reset()
        score.decrease_lives()
        if score.lives == 0:
            score.reset()
            playing_game = False
            ui.game_over(win=False)
            return
        ui.change_color()
        return

def check_collision_with_bricks():
    global ball,bricks, score

    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            score.increase_score()
            brick.quantity-=1
            if brick.quantity ==0:
                brick.clear()
                brick.goto(3000,3000)
                bricks.bricks.remove(brick)

            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True,y_bounce=False)

#             from bottom
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

def check_collision_with_paddle():
    global ball, paddle
    paddle_x = paddle.xcor()
    ball_x = ball.xcor()


    if ball.distance(paddle) < 110 and ball.ycor() < -250:
#         if paddle right of screen
        if paddle_x > 0:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        #if paddle on left of screen
        elif paddle_x < 0:
            if ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True,y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return





while playing_game:

    if not game_paused:
        win.update()
        time.sleep(0.09)
        ball.move()

        check_collision_with_walls()
        check_collision_with_paddle()
        check_collision_with_bricks()

        if len(bricks.bricks) == 0:
            ui.game_over(win=True)
            break
    else:
        ui.paused_status()

tr.mainloop()














