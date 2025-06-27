

import turtle as tr
from paddle import Paddle


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

paddle = Paddle()
win.listen()
win.onkey(key='Left',fun=paddle.move_left)
win.onkey(key='Right',fun=paddle.move_right)

win.update()




tr.mainloop()














