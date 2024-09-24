from pico2d import *
import math



open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('CIRCLE')

    r = 300
    cx = 400
    cy = 300

    for degree in range(0,360,3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy

        clear.canvas_row()
        character.draw_now(x, y)
        delay(0.1)





def run_rectangle():
    print('RECTANGLE')
    pass


# fill here

while (True):
    run_rectangle()
    run_circle()
    break


close_canvas()
