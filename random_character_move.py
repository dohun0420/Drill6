from pico2d import *
import random

open_canvas()

ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

character_x, character_y = 400, 90
hand_x, hand_y = random.randint(50, 750), random.randint(100, 550)
frame = 0
running = True
speed = 5
facing_right = True

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

while running:
    clear_canvas()

    ground.draw(400, 300, 800, 600)
    hand.draw(hand_x, hand_y)

    dx = hand_x - character_x
    dy = hand_y - character_y
    distance = (dx ** 2 + dy ** 2) ** 0.5

    if dx > 0:
        facing_right = True
    else:
        facing_right = False

    if distance > speed:
        character_x += speed * (dx / distance)
        character_y += speed * (dy / distance)
    else:
        hand_x, hand_y = random.randint(50, 750), random.randint(100, 550)

    if facing_right:
        character.clip_draw(frame * 100, 100, 100, 100, character_x, character_y)
    else:
        character.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', character_x, character_y, 100, 100)

    frame = (frame + 1) % 8

    handle_events()

    update_canvas()
    delay(0.03)

close_canvas()