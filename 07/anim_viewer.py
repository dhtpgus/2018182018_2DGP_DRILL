from pico2d import *
import os

open_canvas()
os.chdir('c:/2018182018_2DGP_DRILL/07')

grass = load_image('grass.png')
character = load_image('skulrun.png')

x = 0
frame = 0
while x < 800:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 62, 0, 55, 100, x, 90, 90, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)
    get_events()

close_canvas()
