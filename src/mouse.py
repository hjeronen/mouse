from sprite import Sprite


class Mouse(Sprite):

    alive = True

    def set_alive(self, collision):
        self.alive = not collision
