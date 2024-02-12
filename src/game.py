import pygame
import time
from map import Map
from mouse import Mouse
from cat import Cat
from settings import (width, height,
                      mouse_start_x, mouse_start_y,
                      cat_one_start, cat_two_start,
                      cat_three_start, cat_four_start)


def start():
    images = load_images()
    map = Map()
    map.create_map()
    scale = images[0].get_width()

    mouse = Mouse(mouse_start_x, mouse_start_y)
    cats = [
        Cat(cat_one_start[1], cat_one_start[0]),
        Cat(cat_two_start[1], cat_two_start[0]),
        Cat(cat_three_start[1], cat_three_start[0]),
        Cat(cat_four_start[1], cat_four_start[0])
    ]

    pygame.init()
    display = pygame.display.set_mode(
        (width * scale, height * scale))

    pygame.display.set_caption("Mouse")

    game_loop(mouse, cats, display, map, images, scale)

    pygame.quit()


def game_loop(mouse, cats, display, map, images, scale):
    running = True
    cat_timer = 0
    fps = 60

    while running:
        time.sleep(1/fps)
        check_events(mouse, map)

        if not mouse.alive:
            draw_game_over_display(display, scale)
            continue

        cat_timer += 1
        if cat_timer >= 60:
            move_cats(mouse, cats, map)
            cat_timer = 0

        draw_game_display(display, map, images, scale)

        collision = check_collision(mouse, cats)
        mouse.set_alive(collision)


def load_images():
    images = []
    for name in ["empty", "tile", "mouse", "cat"]:
        images.append(pygame.image.load("./images/" + name + ".png"))

    return images


def draw_game_display(display, map, images, scale):
    display.fill((0, 0, 0))

    for y in range(height):
        for x in range(width):
            tile = map.get_location(x, y)
            display.blit(images[tile], (x*scale, y*scale))

    pygame.display.flip()


def draw_game_over_display(display, scale):
    black = (0, 0, 0)
    green = (0, 255, 0)
    x = width * scale
    y = height * scale
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Game Over', True, green, black)
    textRect = text.get_rect()
    textRect.center = (x//2, y//2)
    display.fill(black)
    display.blit(text, textRect)
    pygame.display.flip()


def check_events(mouse, map):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if mouse.alive and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                handle_event_move_left(mouse, map)
            if event.key == pygame.K_RIGHT:
                handle_event_move_right(mouse, map)
            if event.key == pygame.K_UP:
                handle_event_move_up(mouse, map)
            if event.key == pygame.K_DOWN:
                handle_event_move_down(mouse, map)


def move_mouse(mouse, map, new_x, new_y):
    old_x = mouse.x
    old_y = mouse.y
    mouse.move(new_x, new_y)
    map.move_mouse(old_x, old_y, mouse.x, mouse.y)


def handle_event_move_left(mouse, map):
    x = mouse.x - 1
    y = mouse.y
    if (mouse.is_possible_move(width, height, x, y) and
            map.move_tiles_left(x, y)):
        move_mouse(mouse, map, x, y)


def handle_event_move_right(mouse, map):
    x = mouse.x + 1
    y = mouse.y
    if (mouse.is_possible_move(width, height, x, y) and
            map.move_tiles_right(x, y)):
        move_mouse(mouse, map, x, y)


def handle_event_move_up(mouse, map):
    x = mouse.x
    y = mouse.y - 1
    if (mouse.is_possible_move(width, height, x, y) and
            map.move_tiles_up(x, y)):
        move_mouse(mouse, map, x, y)


def handle_event_move_down(mouse, map):
    x = mouse.x
    y = mouse.y + 1
    if (mouse.is_possible_move(width, height, x, y) and
            map.move_tiles_down(x, y)):
        move_mouse(mouse, map, x, y)


def move_cats(mouse, cats, map):
    distances = map.get_distances(mouse)
    for cat in cats:
        old_x = cat.x
        old_y = cat.y
        cat.move(map, distances)
        map.move_cat(old_x, old_y, cat.x, cat.y)


def check_collision(mouse, cats):
    for cat in cats:
        if (cat.x, cat.y) == (mouse.x, mouse.y):
            return True

    return False


if __name__ == '__main__':
    start()
