class Sprite:

    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y

    def move(self, x, y):
        self.x = x
        self.y = y

    def get_location(self):
        return self.x, self.y

    def is_possible_move(self, map_width, map_height, new_x, new_y):
        if 0 <= new_x < map_width:
            if 0 <= new_y < map_height:
                return True

        return False
