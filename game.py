import pygame
import Settings
from Microscope import Microscope
from Windows import Windows
from Functions import *
from pages import *



windows = Windows("Game", (Settings.varibles['X'], Settings.varibles['Y']))
microscope = Microscope(windows.Windows_size, 50)

page2_object_list = page2_init(windows.scrn)

def main_loop():

    if(Settings.varibles['page'] == 1):
        page1(windows.scrn)    
    elif(Settings.varibles['page'] == 2):
        page2(windows.scrn, page2_object_list)    
    elif(Settings.varibles['page'] == 3):
        page3(windows.scrn)    
    elif(Settings.varibles['page'] == 4):
        page4(windows.scrn)    
    elif(Settings.varibles['page'] == 5):
        page5(windows.scrn)    
    elif(Settings.varibles['page'] == 6):
        page6(windows.scrn)    
    elif(Settings.varibles['page'] == 7):
        page7(windows.scrn)    
    elif(Settings.varibles['page'] == 8):
        page8(windows.scrn)    
    elif(Settings.varibles['page'] == 9):
        page9(windows.scrn)    
    elif(Settings.varibles['page'] == 10):
        page10(windows.scrn)    
    elif(Settings.varibles['page'] == 11):
        page11(windows.scrn)    
    elif(Settings.varibles['page'] == 12):
        page12(windows.scrn)    
    elif(Settings.varibles['page'] == 13):
        page13(windows.scrn)    
    elif(Settings.varibles['page'] == 14):
        page14(windows.scrn)    
    elif(Settings.varibles['page'] == 15):
        page15(windows.scrn)
    elif(Settings.varibles['page'] == 16):
        microscope.microscope_page(windows.scrn)


    pygame.display.update()



if __name__ == '__main__':
    while (Settings.varibles['loop']):
        main_loop()
    pygame.quit()