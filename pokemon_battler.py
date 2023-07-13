import pygame
from pygame_functions import *
screenSize(600,392)
starter_background = makeSprite("sprites/starters.png")
transformSprite(starter_background, 0, 0.5)
moveSprite(starter_background, -20, -35)
showSprite(starter_background)
choosing_starter = True
while choosing_starter is True:
    try:
        starter_choice = int(input("""Choose your starter:
1: Sceptile      2: Blaziken      3: Swampert
Enter choice here: """))
        if starter_choice < 1:
            print("That number is too low. Please enter a valid number from 1-3.")
        elif starter_choice > 3:
            print("That number is too high. Please enter a valid number from 1-3.")
        else:
            choosing_starter = False
    except ValueError:
        print("Please enter a valid number from 1-3")
background_sprite = makeSprite('sprites/battle background.png')
blaziken_sprite = makeSprite("sprites/blaziken final full.png", 33)
eevee_sprite = makeSprite("sprites/eevee.png")
battle_menu = makeSprite("sprites/battle menu.png", 4)
earthquake = makeLabel("EARTHQUAKE", 30, 40, 290, "black", 'Agency FB')
blaze_kick = makeLabel("BLAZE KICK", 30, 230, 290, "black", "Agency FB")
flamethrower = makeLabel("FLAMETHROWER", 30, 40, 343, "black", "Agency FB")
fire_blast = makeLabel("FIRE BLAST", 30, 230, 343, "black", "Agency FB")
showLabel(blaze_kick)
showLabel(earthquake)
showLabel(flamethrower)
showLabel(fire_blast)
current_selection = 0

transformSprite(background_sprite, 0, 2.5)
moveSprite(background_sprite, 0, 0)
showSprite(background_sprite)
showSprite(eevee_sprite)
moveSprite(eevee_sprite, 450, 100, True)
transformSprite(eevee_sprite, 0, 0.35)
moveSprite(blaziken_sprite, 150, 250, True)
showSprite(blaziken_sprite)
transformSprite(blaziken_sprite, 0, 2.6)
showSprite(battle_menu)
transformSprite(battle_menu, 0, 2.55)
moveSprite(battle_menu, 0, 280)

next_frame = clock()
frame = 0
attacking = False

while True:
    if clock() > next_frame:
        frame = (frame + 1)%16
        next_frame += 40 

    tick(12)
    if keyPressed("y"):
        attacking = True
    else:
        changeSpriteImage(blaziken_sprite,0 *16 + frame)

    if keyPressed("right"):
        current_selection = (current_selection + 1)%4
        changeSpriteImage(battle_menu, current_selection)
    elif keyPressed("down"):
        current_selection = (current_selection + 1)%4
        changeSpriteImage(battle_menu, current_selection)
    elif keyPressed("up"):
        current_selection = (current_selection - 1)%4
        changeSpriteImage(battle_menu, current_selection)
    elif keyPressed("left"):
        current_selection = (current_selection - 1)%4
        changeSpriteImage(battle_menu, current_selection)

    if attacking == True:
        for i in range(16):
            changeSpriteImage(blaziken_sprite, 16 + i)
            pause(20, True)
            attacking = False
endWait()