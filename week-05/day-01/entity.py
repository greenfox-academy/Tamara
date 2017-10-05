class Entity(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_entities(self, x, y):
        self.x = x
        self.y = y


class Hero(Entity):

    def __init__(self, x, y):
        super().__init__(x, y)


class Boss(Entity):
    pass
class Skeleton(Entity):
    pass


