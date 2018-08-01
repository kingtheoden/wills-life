from thing import Thing


class VoidSpace(Thing):

    def __init__(self, x, y):
        Thing.__init__(self, x, y)

    def get_colour(self):
        return self.BLACK
