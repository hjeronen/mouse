from sprite import Sprite
from settings import width, height, empty, mouse


class Cat(Sprite):

    def find_possible_moves(self, map):
        """
        Go through adjacent squares and return a list of free spaces.
        Requires the game map as input parameter.
        """
        places = []
        moves = [-1, 0, 1]

        row = self.y - 1
        end = self.y + 1

        while row <= end:
            # check if y coordinate goes over the map
            if row < 0:
                continue

            if row == height:
                break

            # loop through x values on the row
            for move in moves:
                new_x = self.x + move

                if new_x < 0:
                    continue

                if row == self.y and new_x == self.x:
                    continue

                if new_x == width:
                    break

                location_value = map.get_location(new_x, row)
                if location_value == empty or location_value == mouse:
                    places.append((row, new_x))

            row += 1

        return places

    def move(self, map, distances):
        """
        Find the best move, meaning an adjacent square with
        the smallest value.

        Requires a matrix of distances from the mouse and
        the game map as parameters.
        """
        # possible moves on the map
        places = self.find_possible_moves(map)

        # if there are no possible moves, stay put
        if len(places) == 0:
            return

        # smallest value in distances matrix
        best_move = places[0]

        for place in places:
            y = place[0]
            x = place[1]

            if distances[y][x] < distances[best_move[0]][best_move[1]]:
                best_move = place

        self.y = best_move[0]
        self.x = best_move[1]
