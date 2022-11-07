from pico2d import *
import game_world
from ball import Ball
import game_framework
import random

# 새의 크기 가로 30cm, 세로 20cm
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel이 30cm
# 새의 속도 120km/h
RUN_SPEED_KMPH = 120.0  # km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14
# 1 : 이벤트 정의
RD, LD, RU, LU, TIMER, SPACE = range(6)
event_name = ['RD', 'LD', 'RU', 'LU', 'TIMER', 'SPACE']

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}


# 2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir += 1

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')
        if event == SPACE:
            self.fire_ball()

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        # self.frame = (self.frame + 1) % 14
        if self.turn == 0:
            self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
            if self.x >= 1600:
                self.turn = 1
        elif self.turn == 1:
            self.x -= self.dir * RUN_SPEED_PPS * game_framework.frame_time
            if self.x <= 0:
                self.turn = 0

    @staticmethod
    def draw(self):
        if self.turn == 1:
            if self.frame < 5:
                self.image.clip_composite_draw(int(self.frame) * 183, 336, 183, 168, 0, 'h', self.x, self.y, 183, 168)
            elif 5 <= self.frame < 10:
                self.image.clip_composite_draw((int(self.frame)-5) * 183, 168, 183, 168, 0, 'h', self.x, self.y, 183, 168)
            elif 10 <= self.frame < 14:
                self.image.clip_composite_draw((int(self.frame)-10) * 183, 0, 183, 168, 0, 'h', self.x, self.y, 183, 168)

        else:
            if self.frame < 5:
                self.image.clip_draw(int(self.frame) * 183, 336, 183, 168, self.x, self.y)
            elif 5 <= self.frame < 10:
                self.image.clip_draw((int(self.frame) - 5) * 183, 168, 183, 168, self.x, self.y)
            elif 10 <= self.frame < 14:
                self.image.clip_draw((int(self.frame) - 10) * 183, 0, 183, 168, self.x, self.y)


class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir
        if event == SPACE:
            self.fire_ball()

    def do(self):
        # self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1600)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(int(self.frame) * 184, 0, 184, 168, self.x, self.y)


class SLEEP:

    def enter(self, event):
        print('ENTER SLEEP')
        self.frame = 0

    def exit(self, event):
        pass

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 100, 200, 100, 100,
                                           -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100,
                                           3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)


# 3. 상태 변환 구현

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, SPACE: IDLE},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, SPACE: RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, SPACE: IDLE}
}


class Boy:

    def __init__(self):
        # self.x, self.y = 100, 200
        self.x, self.y = random.randint(100, 1000), random.randint(150,500)
        self.frame = random.randint(0, 14)
        self.turn = random.randint(0, 1)
        self.dir, self.face_dir = 0, 1
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f})', (255, 255, 0))

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def fire_ball(self):
        print('FIRE BALL')
        ball = Ball(self.x, self.y, self.face_dir * 2)
        game_world.add_object(ball, 1)
