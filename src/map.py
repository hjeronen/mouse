import math


def check_tile_or_empty(start, end, index):
    return start < index < end


def create_map():
    height = 21
    width = 21

    empty = 0
    tile = 1
    mouse = 2

    # where tiles start and end
    tile_start_x = math.floor(width/4) - 2
    tile_start_y = math.floor(height/4) - 2

    tile_end_x = width - tile_start_x - 1
    tile_end_y = height - tile_start_y - 1

    map = []

    # create map
    for i in range(0, height):
        row = []

        # create rows
        for j in range(0, width):
            x_is_tile = check_tile_or_empty(tile_start_x, tile_end_x, j)
            y_is_tile = check_tile_or_empty(tile_start_y, tile_end_y, i)

            if (x_is_tile & y_is_tile):
                row.append(tile)
            else:
                row.append(empty)

        map.append(row)

    map[math.floor(height/2)][math.floor(width/2)] = mouse

    return map
