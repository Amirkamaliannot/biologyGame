import pygame
import random
import Settings


Settings.varibles['mouse_motion_fram']


def mouse_motion(scrn):

    pygame.mouse.set_visible(False)
    img_name = "images/stable_motion2/frame"+str(Settings.varibles['mouse_motion_fram'])+".png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    motion_fram = pygame.transform.scale(motion_fram, (256, 256))
    pos = pygame.mouse.get_pos()

    frame_height = motion_fram.get_height()
    frame_width = motion_fram.get_width()
    scrn.blit(motion_fram, (pos[0]-frame_width/2, pos[1]-frame_height/2))
    Settings.varibles['mouse_motion_fram'] += 1
    if(Settings.varibles['mouse_motion_fram'] >214):Settings.varibles['mouse_motion_fram']=0

def mouse_hand(scrn, clicked=0):
    pygame.mouse.set_visible(False)

    if(clicked):
        img_name = "images/mouse_hand_clicked.png"
    else:
        img_name = "images/mouse_hand.png"

    image = pygame.image.load(img_name).convert_alpha()
    image = pygame.transform.scale(image, (40, 43))
    pos = pygame.mouse.get_pos()

    image_height = image.get_height()
    image_width = image.get_width()
    scrn.blit(image, (pos[0]-image_width/2, pos[1]-image_height/2))

