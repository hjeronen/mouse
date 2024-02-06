import pygame
from map import Map
from mouse import Mouse
from settings import width, height, mouse_start_x, mouse_start_y


def start():
    images = load_images()
    map = Map()
    map.create_map()
    scale = images[0].get_width()

    mouse = Mouse(mouse_start_x, mouse_start_y)

    pygame.init()
    display = pygame.display.set_mode(
        (width * scale, height * scale))

    pygame.display.set_caption("Mouse")

    running = True

    while running:
        check_events(mouse, map)
        draw_display(display, map, images, scale)
        pygame.display.flip()

    pygame.quit()


def load_images():
    images = []
    for name in ["empty", "tile", "mouse", "cat"]:
        images.append(pygame.image.load("./images/" + name + ".png"))

    return images


def draw_display(display, map, images, scale):
    display.fill((0, 0, 0))

    for y in range(height):
        for x in range(width):
            tile = map.get_location(x, y)
            display.blit(images[tile], (x*scale, y*scale))


def check_events(mouse, map):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
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


if __name__ == '__main__':
    start()
