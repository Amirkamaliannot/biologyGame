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
        self.zoom = 1


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


            "4X":                [(32 , 865), (230,1032), 0],
            "10X":               [(38 , 683), (227, 852), 0],
            "40X":               [(275, 865), (472,1030), 0],
            "100X":              [(281, 685), (476, 849), 0]
        }


        self.left_padding = (0.6406* self.X) - self.image_x_size/2
        self.up_padding = (0.5* self.Y) - self.image_y_size/2

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



        if(self.button_pos["moveX+"][2]):
            self.img_x += 10
        if(self.button_pos["moveX-"][2]):                
            self.img_x -= 10
        if(self.button_pos["moveY+"][2]):                   
            self.img_y += 10
        if(self.button_pos["moveY-"][2]):
            self.img_y -= 10    
        if(self.button_pos["brighten_inc"][2]):
            self.brighten += 10    
        if(self.button_pos["brighten_dec"][2]):
            self.brighten -= 10    
        if(self.button_pos["fast_adjust+"][2]):
            self.adjust_value += 0.6    
        if(self.button_pos["fast_adjust-"][2]):
            self.adjust_value -= 0.6  
        if(self.button_pos["slow_adjust+"][2]):
            self.adjust_value += 0.1    
        if(self.button_pos["slow_adjust-"][2]):
            self.adjust_value -= 0.1        
            

        #zooming functionality
        zoom = False
        if(self.button_pos["4X"][2] and self.zoom != 1):
            zoom = 1
            self.zoom = 1   
        elif(self.button_pos["10X"][2] and self.zoom != 2):
            zoom = 1.5
            self.zoom = 2        
        elif(self.button_pos["40X"][2] and self.zoom != 3):
            zoom = 2.2
            self.zoom = 3       
        elif(self.button_pos["100X"][2] and self.zoom != 4):
            zoom = 4.2
            self.zoom = 4

        if(zoom):
            self.scale_y = zoom
            self.scale_x = zoom
            center_rate_x =((0.6406* self.X) -(-self.img_x + self.left_padding))/self.image_x_size
            center_rate_y =((0.5* self.Y) -(-self.img_y + self.up_padding))/self.image_y_size 
            self.image_x_size = self.X*self.scale_x 
            self.image_y_size = self.Y*self.scale_y
            self.img_x = ((0.6406* self.X) - self.image_x_size * center_rate_x - self.left_padding) * -1
            self.img_y = ((0.5* self.Y) - self.image_y_size * center_rate_y - self.up_padding) * -1  




        if self.adjust_value  > 2.7 :
            self.adjust_value = 2.7    
        if self.adjust_value  < -2.7 :
            self.adjust_value = -2.7

        


        # Get the state of the keys
        keys = pygame.key.get_pressed()
        # Move the image based on the key presses

        if keys[pygame.K_LEFT]:
            self.img_x -= 20
        if keys[pygame.K_RIGHT]:
            self.img_x += 20
        if keys[pygame.K_UP]:
            self.img_y -= 20
        if keys[pygame.K_DOWN]:
            self.img_y += 20
        if keys[pygame.K_w]:
            self.adjust_value += 0.2
        if keys[pygame.K_s]:
            self.adjust_value -= 0.2
        
        if keys[pygame.K_i]:
            self.brighten += 5
        if keys[pygame.K_k]:
            self.brighten -= 5
        if self.brighten < 0:
            self.brighten = 0    
        if self.brighten > 240:
            self.brighten = 240


        #keep in box
        if( -(self.img_x -self.left_padding) > self.start_scope_x):
            self.img_x = -(self.start_scope_x - self.left_padding)

        if(self.image_x_size-self.img_x < self.end_scope_x):

            self.img_x = -(self.end_scope_x - self.image_x_size)

        if(self.img_y < 0):
            self.img_y = 0
        if(self.img_y + self.Y > self.image_y_size):
            self.img_y = self.image_y_size - self.Y


    def microscope_show(self, scrn):
        image = self.imp.copy()
        amt = abs(self.adjust_value) * 20  + 1
        image = Functions.blurSurf(image, amt)
        image.fill((self.brighten, self.brighten, self.brighten), special_flags=pygame.BLEND_RGB_ADD) 
        image = pygame.transform.scale(image, (int(self.image_x_size), int(self.image_y_size)))


        scrn.blit(image, (-self.img_x + self.left_padding , -self.img_y+ self.up_padding))

        scrn.blit(self.mocroscope_template, (0, 0))


        scrn.blit(self.green_border, ( -1230-self.left_padding , 300))

        #green border for microscope_zoom_buttom
        if(self.zoom ==1):
            scrn.blit(self.green_border, (30, 854))
        elif(self.zoom ==2):
            scrn.blit(self.green_border, (30, 675))
        elif(self.zoom ==3):
            scrn.blit(self.green_border, (275, 854))
        elif(self.zoom ==4):
            scrn.blit(self.green_border, (275, 675))


    def microscope_page(self, scrn):
        pygame.mouse.set_visible(True)
        self.microscope_update()
        self.microscope_show(scrn)