class Entity(object):
    def __init__(self):
        pass


class Hero(Entity):

    def __init__(self):
        self.x = 0
        self.y = 0

class Boss(Entity):
    pass
class Skeleton(Entity):
    pass

hero = Hero()
