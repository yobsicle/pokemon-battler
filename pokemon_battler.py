import pygame
from pygame_functions import *

screenSize(600,600) 
setBackgroundColour('dark green')
blaziken_sprite = makeSprite("sprites/blaziken final full.png", 33)
eevee_sprite = makeSprite("sprites/eevee.png")

earthquake = makeLabel("Earthquake", 32, 100, 100, "green", 'Pokemon')
showLabel(earthquake)

showSprite(eevee_sprite)
moveSprite(eevee_sprite, 500, 150, True)
transformSprite(eevee_sprite, 0, 0.4)
moveSprite(blaziken_sprite, 150, 350, True)
showSprite(blaziken_sprite)
transformSprite(blaziken_sprite, 0, 2.5)

next_frame = clock()
frame = 0
attacking = False

while True:
    if clock() > next_frame:
        frame = (frame + 1)%16
        next_frame += 40 

    tick(120)
    if keyPressed("right"):
        attacking = True
    else:
        changeSpriteImage(blaziken_sprite,0 *16 + frame)
        
    if attacking == True:
        for i in range(16):
            changeSpriteImage(blaziken_sprite, 16 + i)
            pause(20, True)
            attacking = False
endWait()