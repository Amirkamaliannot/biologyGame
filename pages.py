import pygame
import random
import settings


settings.init()
settings.update('width', 600)


exit()

def page1_update():
    global page, loop

    for event in pygame.event.get():
                
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            #left click
            if(event.button == 1):
                page += 1

def page1_show():


    img_name = "pages/page1.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    mouse_motion()

def page1():
    page1_update()
    page1_show()

def page2_update():
    global page, loop

    for event in pygame.event.get():
                
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            #left click
            if(event.button == 1):
                page += 1
            #right click            
            if(event.button == 3):
                page -= 1

                

def page2_show():


    img_name = "pages/page2.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    mouse_motion()

def page2():
    page2_update()
    page2_show()