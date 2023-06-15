import pygame
from pygame_functions import *

screenSize(600,600) 
setBackgroundColour('dark green')
blaziken_sprite = makeSprite("blaziken final full.png", 33)

moveSprite(blaziken_sprite, 300, 300, True)
showSprite(blaziken_sprite)

endWait()
