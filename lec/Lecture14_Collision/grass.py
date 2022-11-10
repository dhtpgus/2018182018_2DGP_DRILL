from pico2d import *


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        draw_rectangle(*self.get_bb())  # tuple 값을 나눠서 인자로 분배하기위해 * 을 사용

    def get_bb(self):
        return 0, 0, 1600 - 1, 50
