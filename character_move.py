from pico2d import *
import math

open_canvas()
 

grass = load_image('grass.png')
boy = load_image('character.png')

def row_circle():
    print('CIRCLE')

    clear.canvas_row()
    boy.draw_now(400, 300)
    
    pass


def row_rectangle():
    print('RECTANGLE')
    pass


# fill here

while (True):
    row_rectangle()
    row_circle()
    break


close_canvas()
