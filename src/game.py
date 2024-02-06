import pygame
from map import create_map


def start():
    images = load_images()
    map = create_map()
    scale = images[0].get_width()

    width = len(map[0])
    height = len(map)

    pygame.init()
    display = pygame.display.set_mode((width * scale, height * scale))

    pygame.display.set_caption("Mouse")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_display(display, width, height, map, images, scale)
        pygame.display.flip()

    pygame.quit()


def load_images():
    images = []
    for name in ["empty", "tile", "mouse", "cat"]:
        images.append(pygame.image.load("./images/" + name + ".png"))

    return images


def draw_display(display, width, height, map, images, scale):
    display.fill((0, 0, 0))

    for y in range(height):
        for x in range(width):
            tile = map[y][x]
            display.blit(images[tile], (x*scale, y*scale))


if __name__ == '__main__':
    start()
