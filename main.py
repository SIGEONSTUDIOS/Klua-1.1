from Klua import *
from Renderer import *
import sys
sys.dont_write_bytecode = True

DEBUG(False, None) #crashes without, change it to True to debug,
#change None to something like kprint to debug kprint




win, canvas = window("TESTING", "200x100")
makeobject_2D(canvas, "triangle", 10, "blue", 400, 300)
makeobject_2D(canvas, "triangle", 3, "blue", 800, 600)
openwindow(win)