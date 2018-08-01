import pygame

from bunny import Bunny
from bush import Bush
from drawer import Drawer
from land import Land
from controller import Controller
from random import random

# Set the initial specs
from wolf import Wolf


class Player:
    def __init__(self):
        self.game_size = 100
        self.ticks_per_second = 60

        screen_size_x = 800
        screen_size_y = 800

        self.land = Land(self.game_size)
        self.drawer = Drawer(screen_size_x, screen_size_y, self.land)
        self.controller = Controller(self.land, self.drawer)

    def random_setup(self):
        for x in range(self.game_size):
            for y in range(self.game_size):

                num = random()
                if num < 0.01:  # 1% bunnies
                    thing = Bunny(x, y)
                    self.controller.put(thing)
                elif num < 0.015:  # 0.5% wolves
                    thing = Wolf(x, y)
                    self.controller.put(thing)
                elif num < 0.35:  # 30% bushes
                    thing = Bush(x, y)
                    self.controller.put(thing)
                else:  # 60% empty space
                    pass  # and 100% reason to remember the name <---- joke comment, disregard

    def small_setup(self):

        bunny = Wolf(0, 20)
        self.controller.put(bunny)

        bunny = Wolf(8, 30)
        self.controller.put(bunny)

        bunny = Bunny(1, 20)
        self.controller.put(bunny)

        bunny = Bunny(2, 20)
        self.controller.put(bunny)

        bunny = Bunny(3, 20)
        self.controller.put(bunny)

        bunny = Bunny(8, 20)
        self.controller.put(bunny)

        bunny = Bunny(8, 25)
        self.controller.put(bunny)

    def play(self):
        # Loop until the user clicks the close button.
        done = False
        pause = False
        clock = pygame.time.Clock()

        self.drawer.draw(self.controller.land)  # draw the entire canvas

        tick_count = 0

        while not done:

            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONUP:
                    pause = not pause

            tick_count += 1

            if not pause:
                self.controller.tick()
                # controller.print_tmi()
                # print(tick_count)
                # print()

            # This limits the while loop to a max of 60 times per second.
            # Leave this out and we will use all CPU we can.
            clock.tick(self.ticks_per_second)

        # Be IDLE friendly
        pygame.quit()
