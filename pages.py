import pygame
import random
import Settings
import Mouse
import Functions




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
def page2_init(scrn):
    object_list = []
    for i in range (10):
        scrn_h = scrn.get_height()
        scrn_w = scrn.get_width()

        pos = (random.randint(0, scrn_w*0.8),  random.randint(scrn_h *0.4, scrn_h * 0.8))
        pygame.image.load("images/moving-img"+str(i)+".png").convert_alpha().get_width
        object_list.append( {"img":pygame.image.load("images/moving-img"+str(i)+".png").convert_alpha(), 
                             'pos':pos, 
                             'clicked':False,
                             'click_pos' : (0,0)
                             })
    return object_list


def page2_update(object_list):

    for event in pygame.event.get():
                
        if event.type == pygame.QUIT:
            Settings.varibles['loop'] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            for i in list(reversed(range(len(object_list)))):
                in_box = Functions.is_in_button(pos,  
                                                    (
                                                        object_list[i]['pos'], 
                                                        (object_list[i]['pos'][0]+ object_list[i]['img'].get_width(), object_list[i]['pos'][1]+ object_list[i]['img'].get_height() )
                                                    )
                                                )
                if(event.button == 1 and in_box):
                    for j in range(len(object_list)):
                        object_list[j]['clicked'] = False

                    object_list[i]['clicked'] = True
                    object_list[i]['click_pos'] = ( pos[0]-object_list[i]['pos'][0], pos[1]-object_list[i]['pos'][1])
                    
                    break

                else:
                    object_list[i]['clicked'] = False

            # left click
            if(event.button == 1 and Functions.is_in_button(pos, ((0,20), (0 + 90, 20+60)))):
                Settings.varibles['page'] += 1
            #right click            
            if(event.button == 3):
                Settings.varibles['page'] -= 1

        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            for j in range(len(object_list)):
                object_list[j]['clicked'] = False


        for j in range(len(object_list)):
            if(object_list[j]['clicked']):
                pos = pygame.mouse.get_pos()
                object_list[j]['pos'] = (pos[0] - object_list[j]['click_pos'][0], pos[1] - object_list[j]['click_pos'][1]) 

    return object_list

                

def page2_show(scrn, object_list):

    click = 0

    img_name = "images/pages/page2.png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    scrn.blit(motion_fram, (0,0))    
    
    next_icon = "images/next.png"
    next_icon = pygame.image.load(next_icon).convert_alpha()
    scrn.blit(next_icon, (0,20))    
    
    perv_icon = "images/perv.png"
    perv_icon = pygame.image.load(perv_icon).convert_alpha()
    scrn.blit(perv_icon, (scrn.get_width()- perv_icon.get_width(),20))

    for i in object_list:

        obj = i["img"]
        if(i['clicked']):

            copy = obj.copy()
            copy.fill((60, 60, 60), special_flags=pygame.BLEND_RGB_ADD) 
            scrn.blit(copy, i['pos'])

            click = 1
        else:
            scrn.blit(obj, i['pos'])

    Mouse.mouse_hand(scrn, click)

    return object_list

def page2(scrn, object_list):

    object_list = page2_update(object_list)
    print
    object_list = page2_show(scrn, object_list)

    return object_list




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


