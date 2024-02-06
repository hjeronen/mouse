from sprite import Sprite
from settings import width, height, empty, mouse, tile


class Cat(Sprite):

    def find_possible_moves(self, map):
        places = []
        moves = [-1, 0, 1]

        row = self.y - 1
        end = self.y + 1

        while row <= end:
            if row < 0:
                continue

            if row == height:
                break

            for move in moves:
                new_x = self.x + move

                if new_x < 0:
                    continue

                if row == self.y and new_x == self.x:
                    continue

                if new_x == width:
                    break

                if map[row][self.x + move] != tile:
                    places.append((row, new_x))

            row += 1

        return places

    def move(self, map):
        places = self.find_possible_moves(map)
        best_move = places[0]

        for place in places:
            y = place[0]
            x = place[1]

            if map[y][x] < map[best_move[0]][best_move[1]]:
                best_move = place

        self.y = best_move[0]
        self.x = best_move[1]
