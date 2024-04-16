import pygame
import random



class Microscope():
    def __init__(self, magnification):
        self.magnification = magnification

        self.imp = pygame.image.load("pathology_irondeficiencyanemia20x03-transformed (1).jpeg").convert()
        self.gear_1 = pygame.image.load('707024_gear_512x512.png').convert_alpha()
        self.gear_1 = pygame.transform.scale(gear_1, (30, 30))

        self.mocroscope_template = pygame.image.load('mocroscope_template.png').convert_alpha()
        self.mocroscope_template = pygame.transform.scale(mocroscope_template, (X, Y))

        self.green_border = pygame.image.load('green_border.png').convert_alpha()
        self.green_border = pygame.transform.scale(green_border, (205, 185))

        self.start_scope_x = int(X/2.7428)
        self.end_scope_x = int(X/1.097)

        
        self.scale_x = 1
        self.scale_y = 1
        self.scale_step = 0.5
        self.img_x = 0
        self.img_y = 0
        self.image_x_size= X*scale_x
        self.image_y_size = Y*scale_y