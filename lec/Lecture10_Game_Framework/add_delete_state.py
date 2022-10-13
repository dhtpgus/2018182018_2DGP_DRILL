from pico2d import *
import game_framework
import play_state

image = None

a=1

def enter():
    global image
    image = load_image('add_delete_boy.png')
    pass


def exit():
    global image
    del image
    # fill here
    pass


def update():
    pass


def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()
    # fill here
    pass


def handle_events():
    global a
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_KP_PLUS:
                    play_state.boy.item = 'boy_plus'
                    a+=1
                    game_framework.pop_state()
                case pico2d.SDLK_KP_MINUS:
                    play_state.boy.item = 'boy_minus'
                    a-=1
                    game_framework.pop_state()
