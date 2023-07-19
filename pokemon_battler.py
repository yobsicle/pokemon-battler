# base level calibration stuff for pygame.
import pygame
from pygame_functions import *
import random
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
        showLabel(moves[0]["name"])
        showLabel(moves[1]["name"])
        showLabel(moves[2]["name"])
        showLabel(moves[3]["name"])
    elif hide_or_show == "hide":
        hideLabel(moves[0]["name"])
        hideLabel(moves[1]["name"])
        hideLabel(moves[2]["name"])
        hideLabel(moves[3]["name"])


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


def calc_damage(target_stats, move):
    type_multiplier = type_effectiveness[move["type"]][target_stats["type"]] * type_effectiveness[move["type"]][target_stats["type 2"]]
    if move["stab"] is True:
        stab_multi = 1.5
    else:
        stab_multi = 1
    if random.randint(0,100) <= move["accuracy"]:
        pass
    else:
        damage = 0
    # return damage
    print(type_multiplier)

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
# type effectiveness chart
type_effectiveness = {"FIRE": {"FIRE": 0.5, "WATER": 0.5, "GRASS": 2, "NORMAL": 1, "FIGHTING": 1, "GROUND": 1, "DRAGON": 0.5,
                               "STEEL": 2, "DARK": 1, "FLYING": 1, "PSYCHIC": 1, "BUG": 2, "NONE": 1}, 
                      "NORMAL": {"FIRE": 1, "WATER": 1, "GRASS": 1, "NORMAL": 1, "FIGHTING": 1, "GROUND": 1, "DRAGON": 1,
                                 "STEEL": 0.5, "DARK": 1, "FLYING": 1, "PSYCHIC": 1, "BUG": 1, "NONE": 1}, 
                      "WATER": {"FIRE": 2, "WATER": 1, "GRASS": 0.5, "NORMAL": 1, "FIGHTING": 1, "GROUND": 2, "DRAGON": 0.5,
                                "STEEL": 1, "DARK": 1, "FLYING": 1, "PSYCHIC": 1, "BUG": 1, "NONE": 1},
                      "GRASS": {"FIRE": 0.5, "WATER": 2, "GRASS": 0.5, "NORMAL": 1, "FIGHTING": 1, "GROUND": 2, "DRAGON": 0.5,
                                "STEEL": 0.5, "DARK": 1, "FLYING": 0.5, "PSYCHIC": 1, "BUG": 0.5, "NONE": 1},
                      "FIGHTING": {"FIRE": 1, "WATER": 1, "GRASS": 1, "NORMAL": 2, "FIGHTING": 1, "GROUND": 1, "DRAGON": 1,
                                   "STEEL": 2, "DARK": 2, "FLYING": 0.5, "PSYCHIC": 0.5, "BUG": 0.5, "NONE": 1},
                      "GROUND": {"FIRE": 2, "WATER": 1, "GRASS": 0.5, "NORMAL": 1, "FIGHTING": 1, "GROUND": 1, "DRAGON": 1,
                                 "STEEL": 2, "DARK": 1, "FLYING": 0, "PSYCHIC": 1, "BUG": 0.5, "NONE": 1},
                      "DRAGON": {"FIRE": 1, "WATER": 1, "GRASS": 1, "NORMAL": 1, "FIGHTING": 1, "GROUND": 1, "DRAGON": 2,
                                 "STEEL": 0.5, "DARK": 1, "FLYING": 1, "PSYCHIC": 1, "BUG": 1, "NONE": 1},
                      "STEEL": {"FIRE": 0.5, "WATER": 0.5, "GRASS": 1, "NORMAL": 1, "FIGHTING": 1, "GROUND": 1, "DRAGON": 1,
                                "STEEL": 0.5, "DARK": 1, "FLYING": 1, "PSYCHIC": 1, "BUG": 1, "NONE": 1},
                      "DARK": {"FIRE": 1, "WATER": 1, "GRASS": 1, "NORMAL": 1, "FIGHTING": 0.5, "GROUND": 1, "DRAGON": 1,
                               "STEEL": 1, "DARK": 0.5, "FLYING": 1, "PSYCHIC": 2, "BUG": 1, "NONE": 1},
                      "FLYING": {"FIRE": 1, "WATER": 1, "GRASS": 2, "NORMAL": 1, "FIGHTING": 2, "GROUND": 1, "DRAGON": 1,
                                  "STEEL": 0.5, "DARK": 1, "FLYING": 1, "PSYCHIC": 1, "BUG": 2, "NONE": 1},
                      "PSYCHIC": {"FIRE": 1, "WATER": 1, "GRASS": 1, "NORMAL": 1, "FIGHTING": 2, "GROUND": 1, "DRAGON": 1,
                                  "STEEL": 0.5, "DARK": 0, "FLYING": 1, "PSYCHIC": 0.5, "BUG": 1, "NONE": 1},
                      "BUG": {"FIRE": 0.5, "WATER": 1, "GRASS": 2, "NORMAL": 1, "FIGHTING": 0.5, "GROUND": 1, "DRAGON": 1,
                                  "STEEL": 0.5, "DARK": 2, "FLYING": 0.5, "PSYCHIC": 2, "BUG": 1, "NONE": 1},
                      "NONE": {"FIRE": 1, "WATER": 1, "GRASS": 1, "NORMAL": 1, "FIGHTING": 1, "GROUND": 1, "DRAGON": 1,
                                  "STEEL": 1, "DARK": 1, "FLYING": 1, "PSYCHIC": 1, "BUG": 1, "NONE": 1}}
# stats for all pokemon
eevee_stats = {"type": "NORMAL", "health": 100, "defense": 100}
blaziken_stats = {"type": "FIRE", "type 2": "FIGHTING", "health": 100, "defense": 100}
swampert_stats = {"type": "WATER", "type 2": "GROUND", "health": 100, "defense": 100}
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
    # format: move name, damage, accuracy, type, has stab
    moves = ({"name": energy_ball, "damage": 90, "accuracy": 100, "type": "GRASS", "stab": True},
             {"name": x_scissor, "damage": 80, "accuracy": 100, "type": "BUG", "stab": False},
             {"name": iron_tail, "damage": 100, "accuracy": 80, "type": "STEEL", "stab": False},
             {"name": brick_break, "damage": 75, "accuracy": 100, "type": "FIGHTING", "stab": False})
elif starter_choice == 2:
    moves = ({"name": earthquake, "damage": 100, "accuracy": 100, "type": "GROUND", "stab": False},
             {"name": blaze_kick, "damage": 85, "accuracy": 90, "type": "FIRE", "stab": True},
             {"name": flamethrower, "damage": 90, "accuracy": 100, "type": "FIRE", "stab": True},
             {"name": fire_blast, "damage": 110, "accuracy": 85, "type": "FIRE", "stab": True})
elif starter_choice == 3:
    moves = ({"name": earthquake, "damage": 100, "accuracy": 100, "type": "GROUND", "stab": True},
             {"name": hydro_pump, "damage": 110, "accuracy": 85, "type": "WATER", "stab": True},
             {"name": hammer_arm, "damage": 100, "accuracy": 90, "type": "FIGHTING", "stab": False},
             {"name": water_pulse, "damage": 60, "accuracy": 100, "type": "WATER", "stab": True})
eevee_moves = ({})
calc_damage(swampert_stats, moves[0])

hide_show_moves("show")
current_move = 0

# setup for the clock function
next_frame = clock()
frame = 0
attacking = False

damage_acc = makeLabel("", 0, 0, 0)
move_type = makeLabel("", 0, 0, 0)
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
    # make the damage/acc label
    hideLabel(damage_acc)
    damage_acc = makeLabel(f"{moves[current_move]['damage']}/{moves[current_move]['accuracy']}", 26, 526, 302, "black", "Agency FB")
    showLabel(damage_acc)

    # make the move type label
    hideLabel(move_type)
    move_type = makeLabel(f"{moves[current_move]['type']}", 28, 485, 344, "black", "Agency FB")
    showLabel(move_type)

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
        current_move = (current_move + 1)%4
    elif keyPressed("down"):
        current_selection = (current_selection + 1)%4
        changeSpriteImage(battle_menu, current_selection)
        current_move = (current_move + 1)%4
    elif keyPressed("up"):
        current_selection = (current_selection - 1)%4
        changeSpriteImage(battle_menu, current_selection)
        current_move = (current_move - 1)%4
    elif keyPressed("left"):
        current_selection = (current_selection - 1)%4
        changeSpriteImage(battle_menu, current_selection)
        current_move = (current_move - 1)%4

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