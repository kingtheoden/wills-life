from thing import Thing


class EmptySpace(Thing):

    def __init__(self, x, y):
        Thing.__init__(self, x, y)

    def get_colour(self):
        return self.GREY
