# base level calibration stuff for pygame.
import pygame
from pygame_functions import *
screenSize(600,392)
starter_background = makeSprite("sprites/starters.png")
transformSprite(starter_background, 0, 0.5)
moveSprite(starter_background, -20, -35)
showSprite(starter_background)

# run a loop that lets the user choose a starter.
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


# functions that hide/show certain things.
def hide_show_moves(hide_or_show):
    if hide_or_show == "show":
        showLabel(moves[0][0])
        showLabel(moves[1][0])
        showLabel(moves[2][0])
        showLabel(moves[3][0])
    elif hide_or_show == "hide":
        hideLabel(moves[0][0])
        hideLabel(moves[1][0])
        hideLabel(moves[2][0])
        hideLabel(moves[3][0])



def hide_show_damage_acc(hide_or_show):
    if hide_or_show == "show":
        showLabel(damage_acc_1)
        showLabel(damage_acc_2)
        showLabel(damage_acc_3)
        showLabel(damage_acc_4)
    elif hide_or_show == "hide":
        hideLabel(damage_acc_1)
        hideLabel(damage_acc_2)
        hideLabel(damage_acc_3)
        hideLabel(damage_acc_4)


def hide_show_starter(hide_or_show):
    if hide_or_show == "show":
        if starter_choice == 1:
            showSprite(sceptile_sprite)
        elif starter_choice == 2:
            showSprite(blaziken_sprite)
        elif starter_choice == 3:
            showSprite(swampert_sprite)
    elif hide_or_show == "hide":
        if starter_choice == 1:
            hideSprite(sceptile_sprite)
        elif starter_choice == 2:
            hideSprite(blaziken_sprite)
        elif starter_choice == 3:
            hideSprite(swampert_sprite)


# create all of the sprites and labels for the game.
background_sprite = makeSprite('sprites/battle background.png')
blaziken_sprite = makeSprite("sprites/blaziken final full.png", 33)
sceptile_sprite = makeSprite('sprites/sceptile final.png', 27)
swampert_sprite = makeSprite('sprites/swampert final.png', 34)
eevee_sprite = makeSprite("sprites/eevee.png")
battle_menu = makeSprite("sprites/battle menu.png", 4)
earthquake = makeLabel("EARTHQUAKE", 30, 40, 290, "black", 'Agency FB')
blaze_kick = makeLabel("BLAZE KICK", 30, 230, 290, "black", "Agency FB")
flamethrower = makeLabel("FLAMETHROWER", 30, 40, 343, "black", "Agency FB")
fire_blast = makeLabel("FIRE BLAST", 30, 230, 343, "black", "Agency FB")
energy_ball = makeLabel("ENERGY BALL", 30, 40, 290, "black", 'Agency FB')
x_scissor = makeLabel("X-SCISSOR", 30, 230, 290, "black", "Agency FB")
iron_tail = makeLabel("IRON TAIL", 30, 40, 343, "black", "Agency FB")
brick_break = makeLabel("BRICK BREAK", 30, 230, 343, "black", "Agency FB")
hydro_pump = makeLabel("HYDRO PUMP", 30, 230, 290, "black", "Agency FB")
hammer_arm = makeLabel("HAMMER ARM", 30, 40, 343, "black", "Agency FB")
water_pulse = makeLabel("WATER PULSE", 30, 230, 343, "black", "Agency FB")
current_selection = 0

# move, show, transform all the sprites and labels so they look right
# and appear in the correct position.
transformSprite(background_sprite, 0, 2.5)
moveSprite(background_sprite, 0, 0)
showSprite(background_sprite)
showSprite(eevee_sprite)
moveSprite(eevee_sprite, 450, 100, True)
transformSprite(eevee_sprite, 0, 0.35)
moveSprite(blaziken_sprite, 150, 250, True)
moveSprite(sceptile_sprite, 150, 250, True)
moveSprite(swampert_sprite, 150, 250, True)
hide_show_starter("show")
transformSprite(blaziken_sprite, 0, 2.6)
transformSprite(sceptile_sprite, 0, 2.6)
transformSprite(swampert_sprite, 0, 2.6)
showSprite(battle_menu)
transformSprite(battle_menu, 0, 2.55)
moveSprite(battle_menu, 0, 280)

if starter_choice == 1:
    moves = ((energy_ball, 90, 100, "grass"),(x_scissor, 80, 100, "bug"), (iron_tail, 100, 80, "steel"), (brick_break, 75, 100, "fighting"))
elif starter_choice == 2:
    moves = ((earthquake, 100, 100, "ground"), (blaze_kick, 85, 90, "fire"), (flamethrower, 90, 100, "fire"), (fire_blast, 110, 85, "fire"))
elif starter_choice == 3:
    moves = ((earthquake, 100, 100, "ground"), (hydro_pump, 110, 85, "water"), (hammer_arm, 100, 90, "fighting"), (water_pulse, 60, 100, "water"))

hide_show_moves("show")
damage_acc_1 = makeLabel(f"{moves[0][1]}/{moves[0][2]}", 30, 0, 0, "black", "Agency FB")
damage_acc_2 = makeLabel(f"{moves[0][1]}/{moves[0][2]}", 30, 0, 0, "black", "Agency FB")
damage_acc_3 = makeLabel(f"{moves[0][1]}/{moves[0][2]}", 30, 0, 0, "black", "Agency FB")
damage_acc_4 = makeLabel(f"{moves[0][1]}/{moves[0][2]}", 30, 0, 0, "black", "Agency FB")
hide_show_damage_acc("show")

next_frame = clock()
frame = 0
attacking = False

# the actual running game
while True:
    if clock() > next_frame:
        if starter_choice == 1:
            frame = (frame + 1)%27
            next_frame += 40 
        elif starter_choice == 2:
            frame = (frame + 1)%16
            next_frame += 40 
        elif starter_choice == 3:
            frame = (frame + 1)%34
            next_frame += 40 

    tick(12)
    if keyPressed("y"):
        attacking = True
    elif starter_choice == 1:
        changeSpriteImage(sceptile_sprite,0 * 13 + frame)
    elif starter_choice == 2:
        changeSpriteImage(blaziken_sprite,0 * 16 + frame)
    elif starter_choice == 3:
        changeSpriteImage(swampert_sprite,0 * 34 + frame)

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
        if starter_choice == 1:
            for i in range(10):
                changeSpriteImage(sceptile_sprite, 10 + i)
                pause(40, True)
            attacking = False
        elif starter_choice == 2:
            for i in range(16):
                changeSpriteImage(blaziken_sprite, 16 + i)
                pause(20, True)
            attacking = False
        elif starter_choice == 3:
            for i in range(10):
                changeSpriteImage(swampert_sprite, i)
                pause(40, True)
            attacking = False
endWait()