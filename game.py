import pygame
import random

import settings


settings.init()
settings.update('width', 600)
settings.update('page', 1)


class windows():

    def __init__(self, name, size):
        X = size[0]
        Y = size[1]
 
        # activate the pygame library .
        pygame.init()
        self.scrn = pygame.display.set_mode((X, Y))
        # set the pygame window name
        pygame.display.set_caption(name)




 

 
# create a surface object, image is drawn on it.
imp = pygame.image.load("pathology_irondeficiencyanemia20x03-transformed (1).jpeg").convert()
gear_1 = pygame.image.load('707024_gear_512x512.png').convert_alpha()
gear_1 = pygame.transform.scale(gear_1, (30, 30))


mocroscope_template = pygame.image.load('mocroscope_template.png').convert_alpha()
mocroscope_template = pygame.transform.scale(mocroscope_template, (X, Y))


green_border = pygame.image.load('green_border.png').convert_alpha()
green_border = pygame.transform.scale(green_border, (205, 185))


start_scope_x = int(X/2.7428)
end_scope_x = int(X/1.097)



loop = True
scale_x = 1
scale_y = 1
scale_step = 0.5
img_x = 0
img_y = 0

image_x_size= X*scale_x
image_y_size = Y*scale_y

button_pos = {
    "moveX-":            [(36 , 83 ), (132, 158), 0],
    "moveX+":            [(142, 86 ), (236, 159), 0],
    
    "moveY-":            [(36 , 200), (132, 274), 0],
    "moveY+":            [(137, 201), (233, 271), 0],

    "fast_adjust-":      [(36 , 310), (128, 383), 0],
    "fast_adjust+":      [(138, 312), (233, 385), 0],

    "slow_adjust-":      [(36 , 422), (132, 496), 0],
    "slow_adjust+":      [(138, 426), (232, 498), 0],

    "brighten_inc":      [(251, 541), (489, 641), 0],
    "brighten_dec":      [(22 , 541), (252, 641), 0],

    "5X":                [(32 , 865), (230,1032), 0],
    "10X":               [(38 , 683), (227, 852), 0],
    "40X":               [(275, 865), (472,1030), 0],
    "100X":              [(281, 685), (476, 849), 0]
}



up_padding = 0
left_padding = 300

adjust_value = random.randint(-3000, 3000)/100
brighten = 50


frame_period = 0


from functions import *
from pages import *


def microscope_update():
    global scale_x, scale_y, img_x, img_y, image_x_size, image_y_size, loop, brighten, adjust_value

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # handle MOUSEBUTTONDOWN
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            for button in button_pos.keys():
                if(is_in_button(pos, button_pos[button])):
                    button_pos[button][2] = 1        

        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            for button in button_pos.keys():
                button_pos[button][2] = 0



        if event.type == pygame.QUIT:
            loop = False


        if event.type == pygame.MOUSEWHEEL:

            if(event.y > 0):
                scale_x += scale_step
                scale_y += scale_step
                img_x = img_x + X * (scale_step/2) 
                img_y = img_y + (Y) * (scale_step/2)

            elif (event.y < 0):
                scale_x -= scale_step
                scale_y -= scale_step
                img_x = img_x - X * (scale_step/2)
                img_y = img_y - (Y) * (scale_step/2)

            if(scale_x < 1 or scale_y < 1):
                scale_x = 1
                scale_y = 1
            
            image_x_size = X*scale_x 
            image_y_size = Y*scale_y



    if(button_pos["moveX+"][2]):
        img_x += 10
    if(button_pos["moveX-"][2]):                
        img_x -= 10
    if(button_pos["moveY+"][2]):                   
        img_y += 10
    if(button_pos["moveY-"][2]):
        img_y -= 10    
    if(button_pos["brighten_inc"][2]):
        brighten += 10    
    if(button_pos["brighten_dec"][2]):
        brighten -= 10    
    if(button_pos["fast_adjust+"][2]):
        adjust_value += 0.6    
    if(button_pos["fast_adjust-"][2]):
        adjust_value -= 0.6  
    if(button_pos["slow_adjust+"][2]):
        adjust_value += 0.1    
    if(button_pos["slow_adjust-"][2]):
        adjust_value -= 0.1

    if adjust_value  > 2.7 :
        adjust_value = 2.7    
    if adjust_value  < -2.7 :
        adjust_value = -2.7

    

    # Get the state of the keys
    keys = pygame.key.get_pressed()
    # Move the image based on the key presses
    if keys[pygame.K_w]:
        print(img_x) 

    if keys[pygame.K_LEFT]:
        img_x -= 20
    if keys[pygame.K_RIGHT]:
        img_x += 20
    if keys[pygame.K_UP]:
        img_y -= 20
    if keys[pygame.K_DOWN]:
        img_y += 20
    if keys[pygame.K_w]:
        adjust_value += 0.2
    if keys[pygame.K_s]:
        adjust_value -= 0.2
    
    if keys[pygame.K_i]:
        brighten += 5
    if keys[pygame.K_k]:
        print(brighten)
        brighten -= 5
    if brighten < 0:
        brighten = 0    
    if brighten > 240:
        brighten = 240


    #keep in box
    if( -(img_x -left_padding) > start_scope_x):
        img_x = -(start_scope_x - left_padding)

    if(image_x_size-img_x < end_scope_x):

        img_x = -(end_scope_x - image_x_size)

    if(img_y < 0):
        img_y = 0
    if(img_y + Y > image_y_size):
        img_y = image_y_size - Y


def microscope_show():
    image = imp.copy()
    amt = abs(adjust_value) * 20  + 1
    image = blurSurf(image, amt)
    image.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD) 
    image = pygame.transform.scale(image, (int(image_x_size), int(image_y_size)))
    scrn.blit(image, (-img_x + left_padding , -img_y+ up_padding))


    scrn.blit(mocroscope_template, (0, 0))

    #green border for microscope_zoom_buttom
    scrn.blit(green_border, (275, 675))
    scrn.blit(green_border, (275, 854))
    scrn.blit(green_border, (30, 854))
    scrn.blit(green_border, (30, 675))


def microscope_page():
    microscope_update()
    microscope_show()
    

    

def mouse_motion():
    global frame_period

    pygame.mouse.set_visible(False)
    img_name = "stable_motion2/frame"+str(frame_period)+".png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    motion_fram = pygame.transform.scale(motion_fram, (256, 256))
    pos = pygame.mouse.get_pos()

    frame_height = motion_fram.get_height()
    frame_width = motion_fram.get_width()
    scrn.blit(motion_fram, (pos[0]-frame_width/2, pos[1]-frame_height/2))
    frame_period += 4
    if(frame_period >214):frame_period=0


def main_loop():

    if(page == 1):
        page1()    
    elif(page == 2):
        page2()
    elif(page== 100):
        microscope_page()


    pygame.display.update()



while (loop):
    main_loop()

pygame.quit()