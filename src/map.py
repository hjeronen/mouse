import math
from settings import (width, height, empty, tile,
                      mouse, cat,
                      mouse_start_x, mouse_start_y,
                      cat_one_start, cat_two_start,
                      cat_three_start, cat_four_start)


class Map:

    def __init__(self):
        self.map = []

    def check_tile_or_empty(self, start, end, index):
        return start < index < end

    def create_map(self):

        # where tiles start and end
        tile_start_x = math.floor(width/4) - 2
        tile_start_y = math.floor(height/4) - 2

        tile_end_x = width - tile_start_x - 1
        tile_end_y = height - tile_start_y - 1

        # create map
        for i in range(0, height):
            row = []

            # create rows - set tile or empty
            for j in range(0, width):
                x_is_tile = self.check_tile_or_empty(
                    tile_start_x, tile_end_x, j)
                y_is_tile = self.check_tile_or_empty(
                    tile_start_y, tile_end_y, i)

                if (x_is_tile & y_is_tile):
                    row.append(tile)
                else:
                    row.append(empty)

            self.map.append(row)

        # set mouse
        self.map[mouse_start_y][mouse_start_x] = mouse

        # set cats
        self.map[cat_one_start[1]][cat_one_start[0]] = cat
        self.map[cat_two_start[1]][cat_two_start[0]] = cat
        self.map[cat_three_start[1]][cat_three_start[0]] = cat
        self.map[cat_four_start[1]][cat_four_start[0]] = cat

        return map

    def move_mouse(self, old_x, old_y, new_x, new_y):
        self.map[old_y][old_x] = empty
        self.map[new_y][new_x] = mouse

    def move_tiles_left(self, x, y):
        if x < 0:
            return False
        if self.map[y][x] == cat:
            return False
        if self.map[y][x] == empty:
            self.map[y][x] = tile
            return True
        return self.move_tiles_left(x - 1, y)

    def move_tiles_right(self, x, y):
        if x == width:
            return False
        if self.map[y][x] == cat:
            return False
        if self.map[y][x] == empty:
            self.map[y][x] = tile
            return True
        return self.move_tiles_right(x + 1, y)

    def move_tiles_up(self, x, y):
        if y < 0:
            return False
        if self.map[y][x] == cat:
            return False
        if self.map[y][x] == empty:
            self.map[y][x] = tile
            return True
        return self.move_tiles_up(x, y - 1)

    def move_tiles_down(self, x, y):
        if y == height:
            return False
        if self.map[y][x] == cat:
            return False
        if self.map[y][x] == empty:
            self.map[y][x] = tile
            return True
        return self.move_tiles_down(x, y + 1)

    def get_location(self, x, y):
        return self.map[y][x]

    def get_distances(self, mouse):
        distances = []

        # will be implemented later

        return distances
