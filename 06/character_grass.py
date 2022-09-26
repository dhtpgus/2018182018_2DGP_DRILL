from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character= load_image('character.png')


while (1):
 x = 0
 while ( x < 800 ):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x += 2
    delay(0.01)
 y = 0
 while ( y < 600):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(800,y)
    y += 2
    delay(0.01)
 while ( x>0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,600)
    x -= 2
    delay(0.01)
 while( y > 0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(0,y)
    y-= 2
    delay(0.01)

     

close_canvas()
