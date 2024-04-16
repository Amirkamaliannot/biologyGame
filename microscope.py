import pygame
import random
import Functions
import Settings

class Microscope():
    def __init__(self, windows_size, magnification):


        self.X = windows_size[0]
        self.Y = windows_size[1]
 
        self.magnification = magnification

        self.imp = pygame.image.load("images/microscope_showing.jpeg").convert()

        self.mocroscope_template = pygame.image.load('images/mocroscope_template.png').convert_alpha()
        self.mocroscope_template = pygame.transform.scale(self.mocroscope_template, (self.X, self.Y))

        self.green_border = pygame.image.load('images/green_border.png').convert_alpha()
        self.green_border = pygame.transform.scale(self.green_border, (205, 185))

        self.start_scope_x = int(self.X/2.7428)
        self.end_scope_x = int(self.X/1.097)

        
        self.scale_x = 1
        self.scale_y = 1
        self.scale_step = 0.5
        self.img_x = 0
        self.img_y = 0
        self.image_x_size= self.X* self.scale_x
        self.image_y_size = self.Y* self.scale_y


        self.button_pos = {
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


        self.up_padding = 0
        self.left_padding = 300

        self.adjust_value = random.randint(-3000, 3000)/100
        self.brighten = 50


    def microscope_update(self):

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Settings.varibles["loop"] = False

            # handle MOUSEBUTTONDOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for button in self.button_pos.keys():
                    if(Functions.is_in_button(pos, self.button_pos[button])):
                        self.button_pos[button][2] = 1        

            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                for button in self.button_pos.keys():
                    self.button_pos[button][2] = 0





            if event.type == pygame.MOUSEWHEEL:

                if(event.y > 0):
                    scale_x += self.scale_step
                    scale_y += self.scale_step
                    img_x = img_x + self.X * (self.scale_step/2) 
                    img_y = img_y + (self.Y) * (self.scale_step/2)

                elif (event.y < 0):
                    scale_x -= self.scale_step
                    scale_y -= self.scale_step
                    img_x = img_x - self.X * (self.scale_step/2)
                    img_y = img_y - (self.Y) * (self.scale_step/2)

                if(scale_x < 1 or scale_y < 1):
                    scale_x = 1
                    scale_y = 1
                
                image_x_size = self.X*scale_x 
                image_y_size = self.Y*scale_y



        if(self.button_pos["moveX+"][2]):
            img_x += 10
        if(self.button_pos["moveX-"][2]):                
            img_x -= 10
        if(self.button_pos["moveY+"][2]):                   
            img_y += 10
        if(self.button_pos["moveY-"][2]):
            img_y -= 10    
        if(self.button_pos["brighten_inc"][2]):
            brighten += 10    
        if(self.button_pos["brighten_dec"][2]):
            brighten -= 10    
        if(self.button_pos["fast_adjust+"][2]):
            adjust_value += 0.6    
        if(self.button_pos["fast_adjust-"][2]):
            adjust_value -= 0.6  
        if(self.button_pos["slow_adjust+"][2]):
            adjust_value += 0.1    
        if(self.button_pos["slow_adjust-"][2]):
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
        if( -(img_x -self.left_padding) > self.start_scope_x):
            img_x = -(self.start_scope_x - self.left_padding)

        if(image_x_size-img_x < self.end_scope_x):

            img_x = -(self.end_scope_x - image_x_size)

        if(img_y < 0):
            img_y = 0
        if(img_y + self.Y > image_y_size):
            img_y = image_y_size - self.Y


    def microscope_show(self, scrn):
        image = self.imp.copy()
        amt = abs(self.adjust_value) * 20  + 1
        image = Functions.blurSurf(image, amt)
        image.fill((self.brighten, self.brighten, self.brighten), special_flags=pygame.BLEND_RGB_ADD) 
        image = pygame.transform.scale(image, (int(self.image_x_size), int(self.image_y_size)))

        scrn.blit(image, (-self.img_x + self.left_padding , -self.img_y+ self.up_padding))

        scrn.blit(self.mocroscope_template, (0, 0))

        #green border for microscope_zoom_buttom
        scrn.blit(self.green_border, (275, 675))
        scrn.blit(self.green_border, (275, 854))
        scrn.blit(self.green_border, (30, 854))
        scrn.blit(self.green_border, (30, 675))


    def microscope_page(self, scrn):
        self.microscope_update()
        self.microscope_show(scrn)