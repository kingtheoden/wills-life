import pygame


def to_pygame(y_coord, height):
    """Convert y-coords into pygame coordinates (lower-left => top left)."""
    return height - y_coord


def to_pygame(y_coord, height, obj_height):
    """Convert an object's y-coord into pygame coordinates (lower-left of object => top left in pygame coords)."""
    return height - y_coord - obj_height


class Drawer:

    def __init__(self, screen_size_x, screen_size_y, land):
        self.width = screen_size_x
        self.height = screen_size_y
        self.land_size = land.size

        self.disabled = False

        self.WHITE = (255, 255, 255)

        pygame.init()

        # Set the height and width of the screen
        size = (screen_size_x, screen_size_y)
        self.screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Will's Life")

    def draw(self, land):

        if self.disabled:
            return

        self.screen.fill(self.WHITE)
        rect_height = self.height / land.size
        rect_width = self.width / land.size

        for x in range(land.size):
            for y in range(land.size):

                # find out what it is
                thing = land.get(x, y)
                colour = thing.get_colour()

                # origin is bottom left
                rect_x = x * rect_width
                rect_y = y * rect_height

                # pygame's coordinates have the origin in the top left
                py_rect_y = to_pygame(rect_y, self.height, rect_height)
                py_rect_x = rect_x

                rect = [py_rect_x, py_rect_y, rect_width, rect_height]

                pygame.draw.rect(self.screen, colour, rect, 0)

        pygame.display.flip()

    def update(self, thing_list):

        if self.disabled:
            return

        rect_height = self.height / self.land_size
        rect_width = self.width / self.land_size

        for thing in thing_list:
            colour = thing.get_colour()

            # origin is bottom left
            rect_x = thing.pos_x * rect_width
            rect_y = thing.pos_y * rect_height

            # pygame's coordinates have the origin in the top left
            py_rect_y = to_pygame(rect_y, self.height, rect_height)
            py_rect_x = rect_x

            rect = [py_rect_x, py_rect_y, rect_width, rect_height]

            pygame.draw.rect(self.screen, colour, rect, 0)

        pygame.display.flip()

    def disable(self):
        self.disabled = True

    def enable(self):
        self.disabled = False




