import pygame
import Settings
from Microscope import Microscope
from Windows import Windows


Settings.init()
Settings.update('page', 1)

from Functions import *
from pages import *



frame_period = 0

windows = Windows("Game", (Settings.varibles['X'], Settings.varibles['Y']))
microscope = Microscope(windows.Windows_size, 50)

print(microscope)

    

def mouse_motion():
    global frame_period

    pygame.mouse.set_visible(False)
    img_name = "stable_motion2/frame"+str(frame_period)+".png"
    motion_fram = pygame.image.load(img_name).convert_alpha()
    motion_fram = pygame.transform.scale(motion_fram, (256, 256))
    pos = pygame.mouse.get_pos()

    frame_height = motion_fram.get_height()
    frame_width = motion_fram.get_width()
    windows.scrn.blit(motion_fram, (pos[0]-frame_width/2, pos[1]-frame_height/2))
    frame_period += 4
    if(frame_period >214):frame_period=0


def main_loop():

    if(Settings.varibles['page'] == 1):
        page1(windows.scrn)    
    elif(Settings.varibles['page'] == 2):
        page2(windows.scrn)
    elif(Settings.varibles['page']== 100):
        microscope.microscope_page()


    pygame.display.update()



print(213)

while (Settings.varibles['loop']):
    main_loop()

pygame.quit()