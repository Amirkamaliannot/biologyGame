import pygame
import Settings
from Microscope import Microscope
from Windows import Windows
import Mouse
from Functions import *
from pages import *



windows = Windows("Game", (Settings.varibles['X'], Settings.varibles['Y']))
microscope = Microscope(windows.Windows_size, 50)


def main_loop():

    if(Settings.varibles['page'] == 1):
        page1(windows.scrn)    
    elif(Settings.varibles['page'] == 2):
        page2(windows.scrn)
    elif(Settings.varibles['page']== 100):
        microscope.microscope_page()


    pygame.display.update()



while (Settings.varibles['loop']):
    main_loop()

pygame.quit()