import pygame


#showing image using pay game 


# activate the pygame library .
pygame.init()
X = 1920
Y = 1080
 
# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('image')
 
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

up_padding = 0
left_padding = 300

amt = 2
brighten = 128

def blurSurf(surface, amt):
    """
    Blur the given surface by the given 'amount'.  Only values 1 and greater
    are valid.  Value 1 = no blur.
    """
    if amt < 1.0:
        raise ValueError("Arg 'amt' must be greater than 1.0, passed in value is %s"%amt)
    scale = 1.0/float(amt)
    surf_size = surface.get_size()
    scale_size = (int(surf_size[0]*scale), int(surf_size[1]*scale))
    surf = pygame.transform.smoothscale(surface, scale_size)
    surf = pygame.transform.smoothscale(surf, surf_size)
    return surf


def update():
    global scale_x, scale_y, img_x, img_y, image_x_size, image_y_size, loop, amt, brighten



    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

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

            # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            print(pos)
            # # get a list of all sprites that are under the mouse cursor
            # clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
            # # do something with the clicked sprites...

        if event.type == pygame.QUIT:
            loop = False

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
        amt += 0.5
    if keys[pygame.K_s]:
        amt -= 0.5
    if amt < 1:
        amt = 1    
    
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

    


def show():

    image = imp.copy()
    image = blurSurf(image, amt)
    image.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD) 
    image = pygame.transform.scale(image, (int(image_x_size), int(image_y_size)))
    scrn.blit(image, (-img_x + left_padding , -img_y+ up_padding))

    # scrn.blit(gear_1, ( 200, 20))
    scrn.blit(mocroscope_template, (0, 0))

    scrn.blit(green_border, (275, 675))
    scrn.blit(green_border, (275, 854))
    scrn.blit(green_border, (30, 854))
    scrn.blit(green_border, (30, 675))
    # rect = pygame.Rect(0, 0, X, up_padding)
    # color = (255,255,255)
    # pygame.draw.rect(scrn, color, pygame.Rect(0, 0, X, up_padding))
    
    pygame.display.update()



while (loop):
    update()
    show()

pygame.quit()