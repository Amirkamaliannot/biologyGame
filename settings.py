# Settings.py



def init():
    global varibles
    varibles = {}


    varibles['loop'] = True
    varibles['X'] = 1920
    varibles['Y'] = 1080

    
    varibles['page'] = 100


    varibles['mouse_motion_fram'] = 0

def update(key, value):

    global varibles
    varibles[key] = value


init()





    


