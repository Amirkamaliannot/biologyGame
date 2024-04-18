import pygame
import random
import Settings
import Mouse




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


    img_name = "images/pages/page1.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page1(scrn):
    page1_update()
    page1_show(scrn)





####page2#####
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


    img_name = "images/pages/page2.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page2(scrn):
    page2_update()
    page2_show(scrn)




####page3#####
def page3_update():

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

                

def page3_show(scrn):


    img_name = "images/pages/page3.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page3(scrn):
    page3_update()
    page3_show(scrn)




####page4#####
def page4_update():

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

                

def page4_show(scrn):


    img_name = "images/pages/page4.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page4(scrn):
    page4_update()
    page4_show(scrn)




####page5#####
def page5_update():

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

                

def page5_show(scrn):


    img_name = "images/pages/page5.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page5(scrn):
    page5_update()
    page5_show(scrn)




####page2#####
def page6_update():

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

                

def page6_show(scrn):


    img_name = "images/pages/page6.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page6(scrn):
    page6_update()
    page6_show(scrn)




####page7#####
def page7_update():

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

                

def page7_show(scrn):


    img_name = "images/pages/page7.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page7(scrn):
    page7_update()
    page7_show(scrn)




####page8#####
def page8_update():

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

                

def page8_show(scrn):

    img_name = "images/pages/page8.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page8(scrn):
    page8_update()
    page8_show(scrn)




####page9#####
def page9_update():

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

                

def page9_show(scrn):


    img_name = "images/pages/page9.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page9(scrn):
    page9_update()
    page9_show(scrn)




####page10#####
def page10_update():

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

                

def page10_show(scrn):


    img_name = "images/pages/page10.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page10(scrn):
    page10_update()
    page10_show(scrn)



####page11#####
def page11_update():

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

                

def page11_show(scrn):


    img_name = "images/pages/page11.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page11(scrn):
    page11_update()
    page11_show(scrn)




####page12#####
def page12_update():

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

                

def page12_show(scrn):


    img_name = "images/pages/page12.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page12(scrn):
    page12_update()
    page12_show(scrn)




####page2#####
def page13_update():

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

                

def page13_show(scrn):


    img_name = "images/pages/page13.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page13(scrn):
    page13_update()
    page13_show(scrn)




####page2#####
def page14_update():

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

                

def page14_show(scrn):


    img_name = "images/pages/page14.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page14(scrn):    
    page14_update()
    page14_show(scrn)




####page15#####
def page15_update():

    for event in pygame.event.get():
                
        if event.type == pygame.QUIT:
            Settings.varibles['loop'] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            #left click
            if(event.button == 1):
                Settings.varibles['page'] = 100
            #right click            
            if(event.button == 3):
                Settings.varibles['page'] -= 1

                

def page15_show(scrn):


    img_name = "images/pages/page15.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))

    Mouse.mouse_motion(scrn)

def page15(scrn):
    page15_update()
    page15_show(scrn)


