import pygame
import random
import Functions
import Settings


class Windows():

    def __init__(self, name, size):
        X = size[0]
        Y = size[1]

        self.Windows_size = (X,Y)
 
        # activate the pygame library .
        pygame.init()
        self.scrn = pygame.display.set_mode((X, Y))
        # set the pygame window name
        pygame.display.set_caption(name)