import pygame
import random
import Settings




def page1_update():

    for event in pygame.event.get():
                
        if event.type == pygame.QUIT:
            Settings.varibles['loop'] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            #left click
            if(event.button == 1):
                Settings.varibles['page'] += 1

def page1_show(scrn):


    img_name = "pages/page1.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    # mouse_motion()

def page1(scrn):
    page1_update()
    page1_show(scrn)

def page2_update():

    for event in pygame.event.get():
                
        if event.type == pygame.QUIT:
            Settings.varibles['loop'] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            #left click
            if(event.button == 1):
                Settings.varibles['page'] += 1
            #right click            
            if(event.button == 3):
                Settings.varibles['page'] -= 1

                

def page2_show(scrn):


    img_name = "pages/page2.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    # mouse_motion()

def page2(scrn):
    page2_update()
    page2_show(scrn)