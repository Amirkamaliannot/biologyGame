import pygame


#showing image using pay game 


# activate the pygame library .
pygame.init()
X = 1080
Y = 720
 
# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('image')
 
# create a surface object, image is drawn on it.
imp = pygame.image.load("pathology_irondeficiencyanemia20x03-transformed (1).jpeg").convert()
 

loop = True
scale_x = 1
scale_y = 1
scale_step = 0.5
img_x = 0
img_y = 0

image_x_size= X*scale_x
image_y_size = Y*scale_y




def update():
    global scale_x, scale_y, img_x, img_y, image_x_size, image_y_size, loop

    image = imp.copy()
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        if event.type == pygame.MOUSEWHEEL:

            if(event.y > 0):
                scale_x += scale_step
                scale_y += scale_step
                img_x = img_x + X * (scale_step/2) 
                img_y = img_y + Y * (scale_step/2)

            elif (event.y < 0):
                scale_x -= scale_step
                scale_y -= scale_step
                img_x = img_x - X * (scale_step/2)
                img_y = img_y - Y * (scale_step/2)

            if(scale_x < 1 or scale_y < 1):
                scale_x = 1
                scale_y = 1
            
            image_x_size = X*scale_x
            image_y_size = Y*scale_y

        if event.type == pygame.QUIT:
            loop = False

    # Get the state of the keys
    keys = pygame.key.get_pressed()
    # Move the image based on the key presses
    if keys[pygame.K_w]:
        print(img_x) 

    if keys[pygame.K_LEFT]:
        img_x -= 5
    if keys[pygame.K_RIGHT]:
        img_x += 5
    if keys[pygame.K_UP]:
        img_y -= 5
    if keys[pygame.K_DOWN]:
        img_y += 5


    #keep in box
    if(img_x < 0):
        img_x = 0
    if(img_y < 0):
        img_y = 0
    if(img_x + X > image_x_size):
        img_x = image_x_size - X
    if(img_y + Y > image_y_size):
        img_y = image_y_size - Y

    image = pygame.transform.scale(image, (int(image_x_size), int(image_y_size)))
    image.get_rect(center = (250,120))

    return image


def show(image):
    scrn.blit(image, (-img_x, -img_y))
    pygame.display.flip()



while (loop):

    image = imp.copy()
    image = update()
    show(image)

pygame.quit()