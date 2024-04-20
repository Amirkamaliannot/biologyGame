# Settings.py
import Functions


def init():
    global varibles
    varibles = {}


    varibles['loop'] = True
    varibles['X'] = 1920
    varibles['Y'] = 1080

    
    varibles['page'] = 1


    varibles['mouse_motion_fram'] = 0


    varibles['data_dict'] =  Functions.decompress_images('./data')



def update(key, value):

    global varibles
    varibles[key] = value


init()





    


