import random
from pico2d import *
import game_world
import server

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1600), random.randint(0, 1000)

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(sx, sy)
        #draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        return sx-15, sy-15, sx+15, sy+15

    def handle_collision(self, other, group):
        if group == 'boy:balls':
            game_world.remove_object(self)
            server.count += 1

