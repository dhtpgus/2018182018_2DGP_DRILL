from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global dirx, diry
    global x, y
    global L, R
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
                R = 1
                L = 0
            if event.key == SDLK_LEFT:
                dirx -= 1
                L = 1
                R = 0
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
                R = 1
                L = 0
            if event.key == SDLK_LEFT:
                dirx += 1
                L = 1
                R = 0
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dirx = 0
diry = 0
L = 0
R = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if L == 0 and R == 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif L == 1:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    elif R == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    x += dirx * 1
    y += diry * 1
    handle_events()


close_canvas()




