# base level calibration stuff for pygame.
import pygame
from pygame_functions import *
import random
from variables import *
screenSize(600, 392)
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
if starter_choice == 1:
    starter_choice = "SCEPTILE"
elif starter_choice == 2:
    starter_choice = "BLAZIKEN"
elif starter_choice == 3:
    starter_choice = "SWAMPERT"


# functions that hide/show certain things.
def hide_show_moves(hide_or_show):
    if hide_or_show == "show":
        showLabel(moves[0]["label"])
        showLabel(moves[1]["label"])
        showLabel(moves[2]["label"])
        showLabel(moves[3]["label"])
    elif hide_or_show == "hide":
        hideLabel(moves[0]["label"])
        hideLabel(moves[1]["label"])
        hideLabel(moves[2]["label"])
        hideLabel(moves[3]["label"])


def hide_show_starter(hide_or_show):
    if hide_or_show == "show":
        if starter_choice == "SCEPTILE":
            showSprite(sceptile_sprite)
        elif starter_choice == "BLAZIKEN":
            showSprite(blaziken_sprite)
        elif starter_choice == "SWAMPERT":
            showSprite(swampert_sprite)
    elif hide_or_show == "hide":
        if starter_choice == "SCEPTILE":
            hideSprite(sceptile_sprite)
        elif starter_choice == "BLAZIKEN":
            hideSprite(blaziken_sprite)
        elif starter_choice == "SWAMPERT":
            hideSprite(swampert_sprite)


def calc_damage(target_stats, move):
    type_multiplier = type_effectiveness[move["type"]][target_stats["type"]] * type_effectiveness[move["type"]][target_stats["type 2"]]
    if move["stab"] is True:
        stab_multi = 1.5
    else:
        stab_multi = 1
    if random.randint(0, 100) <= move["accuracy"]:
        damage = move["damage"] * stab_multi * type_multiplier * target_stats["defense"]
    else:
        damage = "missed"
    if type_multiplier == 0:
        damage = "immune"
        effectiveness = ""
        punctuation = ""
    elif type_multiplier >= 2:
        effectiveness = "super"
        punctuation = "!"
    elif type_multiplier <= 0.5:
        effectiveness = "not very"
        punctuation = "..."
    else:
        effectiveness = ""
        punctuation = ""
    print(damage)
    return damage, effectiveness, punctuation


# create all of the sprites and labels for the game.
background_sprite = makeSprite('sprites/battle background.png')
blaziken_sprite = makeSprite("sprites/blaziken final full.png", 33)
sceptile_sprite = makeSprite('sprites/sceptile final.png', 27)
swampert_sprite = makeSprite('sprites/swampert final.png', 34)
eevee_sprite = makeSprite("sprites/eevee.png")
lucario_sprite = makeSprite("sprites/lucario.png")
garchomp_sprite = makeSprite("sprites/garchomp.png")
yveltal_sprite = makeSprite("sprites/yveltal.png")
battle_menu = makeSprite("sprites/battle menu.png", 4)
text_display = makeSprite("sprites/text display.png")
trivia_display = makeSprite("sprites/trivia display.png")
earthquake = makeLabel("EARTHQUAKE", 30, 40, 290, "black", "Agency FB")
blaze_kick = makeLabel("BLAZE KICK", 30, 230, 290, "black", "Agency FB")
flamethrower = makeLabel("FLAMETHROWER", 30, 40, 343, "black", "Agency FB")
fire_blast = makeLabel("FIRE BLAST", 30, 230, 343, "black", "Agency FB")
energy_ball = makeLabel("ENERGY BALL", 30, 40, 290, "black", "Agency FB")
x_scissor = makeLabel("X-SCISSOR", 30, 230, 290, "black", "Agency FB")
iron_tail = makeLabel("IRON TAIL", 30, 40, 343, "black", "Agency FB")
brick_break = makeLabel("BRICK BREAK", 30, 230, 343, "black", "Agency FB")
hydro_pump = makeLabel("HYDRO PUMP", 30, 230, 290, "black", "Agency FB")
hammer_arm = makeLabel("HAMMER ARM", 30, 40, 343, "black", "Agency FB")
water_pulse = makeLabel("WATER PULSE", 30, 230, 343, "black", "Agency FB")
trivia_label = makeLabel("", 30, 50, 50, "white", "Agency FB")
potions = makeSprite("sprites/potions.png")
# stats for all pokemon
eevee_stats = {"type": "NORMAL", "type 2": "NONE", "health": 175, "defense": 1}
lucario_stats = {"type": "FIGHTING", "type 2": "STEEL", "health": 275, "defense": 0.8}
garchomp_stats = {"type": "DRAGON", "type 2": "NONE", "health": 200, "defense": 0.8}
yveltal_stats = {"type": "DARK", "type 2": "FLYING", "health": 175, "defense": 0.6}
if starter_choice == "BLAZIKEN":
    starter_stats = {"type": "FIRE", "type 2": "FIGHTING", "health": 250, "defense": 0.45}
elif starter_choice == "SWAMPERT":
    starter_stats = {"type": "WATER", "type 2": "GROUND", "health": 250, "defense": 0.45}
elif starter_choice == "SCEPTILE":
    starter_stats = {"type": "GRASS", "type 2": "NONE", "health": 250, "defense": 0.45}

# move, show, transform all the sprites and labels so they look right
# and appear in the correct position.
transformSprite(background_sprite, 0, 2.5)
moveSprite(background_sprite, 0, 0)
showSprite(background_sprite)
transformSprite(potions, 0, 2.2)
moveSprite(potions, 10, 50)
moveSprite(eevee_sprite, 450, 100, True)
transformSprite(eevee_sprite, 0, 0.35)
moveSprite(lucario_sprite, 450, 100, True)
transformSprite(lucario_sprite, 0, 0.45)
moveSprite(garchomp_sprite, 450, 100, True)
transformSprite(garchomp_sprite, 0, 0.6)
moveSprite(yveltal_sprite, 420, 110, True)
transformSprite(yveltal_sprite, 0, 0.35)
moveSprite(blaziken_sprite, 150, 250, True)
moveSprite(sceptile_sprite, 150, 250, True)
moveSprite(swampert_sprite, 150, 250, True)
hide_show_starter("show")
transformSprite(blaziken_sprite, 0, 2.6)
transformSprite(sceptile_sprite, 0, 2.6)
transformSprite(swampert_sprite, 0, 2.6)
transformSprite(battle_menu, 0, 2.55)
moveSprite(battle_menu, 0, 280)
transformSprite(text_display, 0, 2.55)
moveSprite(text_display, 0, 280)
showSprite(battle_menu)

if starter_choice == "SCEPTILE":
    # format: move name, damage, accuracy, type, has stab
    moves = ({"name": "ENERGY BALL", "label": energy_ball, "damage": 90, "accuracy": 100, "type": "GRASS", "stab": True},
             {"name": "IRON TAIL", "label": iron_tail, "damage": 100, "accuracy": 80, "type": "STEEL", "stab": False},
             {"name": "X SCISSOR", "label": x_scissor, "damage": 80, "accuracy": 100, "type": "BUG", "stab": False},
             {"name": "BRICK BREAK", "label": brick_break, "damage": 75, "accuracy": 100, "type": "FIGHTING", "stab": False})
elif starter_choice == "BLAZIKEN":
    moves = ({"name": "EARTHQUAKE", "label": earthquake, "damage": 100, "accuracy": 100, "type": "GROUND", "stab": False},
             {"name": "FLAMETHROWER", "label": flamethrower, "damage": 90, "accuracy": 100, "type": "FIRE", "stab": True},
             {"name": "BLAZE KICK", "label": blaze_kick, "damage": 85, "accuracy": 90, "type": "FIRE", "stab": True},
             {"name": "FIRE BLAST", "label": fire_blast, "damage": 110, "accuracy": 85, "type": "FIRE", "stab": True})
elif starter_choice == "SWAMPERT":
    moves = ({"name": "EARTHQUAKE", "label": earthquake, "damage": 100, "accuracy": 100, "type": "GROUND", "stab": True},
             {"name": "HAMMER ARM", "label": hammer_arm, "damage": 100, "accuracy": 90, "type": "FIGHTING", "stab": False},
             {"name": "HYDRO PUMP", "label": hydro_pump, "damage": 110, "accuracy": 85, "type": "WATER", "stab": True},
             {"name": "WATER PULSE", "label": water_pulse, "damage": 60, "accuracy": 100, "type": "WATER", "stab": True})

hide_show_moves("show")
current_move = 0
# setup for the clock function
next_frame = clock()
frame = 0
attacking = False

# some variables set to their defaults.
damage_acc = makeLabel( f"{moves[current_move]['damage']}/{moves[current_move]['accuracy']}", 28, 526, 301, "black", "Agency FB")
move_type = makeLabel(f"{moves[current_move]['type']}", 28, 485, 343, "black", "Agency FB")
showLabel(damage_acc)
showLabel(move_type)
current_enemy = 'EEVEE'
enemy_stats = eevee_stats
enemy_moves = eevee_moves
showSprite(eevee_sprite)
enemy_current_hp = enemy_stats["health"]
player_current_hp = starter_stats["health"]
enemy_hp = makeLabel(f"hp: {round(enemy_current_hp / enemy_stats['health'] * 100, 1)}%", 30, 390, 210, "black", "Agency FB")
player_hp = makeLabel(f"hp: {player_current_hp} / {starter_stats['health']}%", 30, 100, 110, "black", "Agency FB")
current_trainer = "EVAN"
you_won = makeLabel(f"You beat<br>TRAINER {current_trainer}!", 40, 30, 290, "white", "Agency FB")
showLabel(enemy_hp)
showLabel(player_hp)
battle_won = False
# the actual running game
while True:
    # the clock to set the framerate of the animations.
    if clock() > next_frame:
        if starter_choice == "SCEPTILE":
            frame = (frame + 1) % 27
            next_frame += 40
        elif starter_choice == "BLAZIKEN":
            frame = (frame + 1) % 16
            next_frame += 40
        elif starter_choice == "SWAMPERT":
            frame = (frame + 1) % 34
            next_frame += 40

    # program's running framerate.
    tick(12)
    
    # animate the starter.
    if starter_choice == "SCEPTILE":
        changeSpriteImage(sceptile_sprite, 0 * 13 + frame)
    elif starter_choice == "BLAZIKEN":
        changeSpriteImage(blaziken_sprite, 0 * 16 + frame)
    elif starter_choice == "SWAMPERT":
        changeSpriteImage(swampert_sprite, 0 * 34 + frame)

    # run if the user presses the "right" button.
    if keyPressed("right"):
        # increment the current selected move
        current_move = (current_move + 1) % 4
        # change the menu sprite to reflect the selected move
        changeSpriteImage(battle_menu, current_move)
        # change the damage/acc and move type labels to match the current selected move
        changeLabel(damage_acc, f"{moves[current_move]['damage']}/{moves[current_move]['accuracy']}")
        changeLabel(move_type, f"{moves[current_move]['type']}")
    elif keyPressed("down"):
        # increment the current selected move
        current_move = (current_move + 1) % 4
        # change the menu sprite to reflect the selected move
        changeSpriteImage(battle_menu, current_move)
        # change the damage/acc and move type labels to match the current selected move
        changeLabel(damage_acc, f"{moves[current_move]['damage']}/{moves[current_move]['accuracy']}")
        changeLabel(move_type, f"{moves[current_move]['type']}")
    elif keyPressed("up"):
        # increment the current selected move
        current_move = (current_move - 1) % 4
         # change the menu sprite to reflect the selected move
        changeSpriteImage(battle_menu, current_move)
        # change the damage/acc and move type labels to match the current selected move
        changeLabel(damage_acc, f"{moves[current_move]['damage']}/{moves[current_move]['accuracy']}")
        changeLabel(move_type, f"{moves[current_move]['type']}")
    elif keyPressed("left"):
        # increment the current selected move
        current_move = (current_move - 1) % 4
         # change the menu sprite to reflect the selected move
        changeSpriteImage(battle_menu, current_move)
        # change the damage/acc and move type labels to match the current selected move
        changeLabel(damage_acc, f"{moves[current_move]['damage']}/{moves[current_move]['accuracy']}")
        changeLabel(move_type, f"{moves[current_move]['type']}")
    elif keyPressed("return"):
        # hide all the stuff in the way of the move display window.
        hideLabel(damage_acc)
        hideLabel(move_type)
        hide_show_moves("hide")
        hideSprite(battle_menu)
        # show the move diplay window.
        showSprite(text_display)
        # use the damage calc function.
        damage, effectiveness, punctuation = calc_damage(enemy_stats, moves[current_move])
        # make the labels to display the move, it's effectiveness, and if it hit.
        display_move_used = makeLabel(f"{starter_choice} used {moves[current_move]['name']}!", 40, 30, 290, "white", "Agency FB")
        display_effectiveness = makeLabel(f"It was {effectiveness} effective{punctuation}", 40, 30, 330, "white", "Agency FB")
        move_missed = makeLabel("It missed!", 40, 30, 330, "white", "Agency FB")
        immune = makeLabel("It had no effect.", 40, 30, 330, "white", "Agency FB")
        # show the used move.
        showLabel(display_move_used)
        # run if the move misses.
        if damage == "missed":
            # show the move missed label.
            showLabel(move_missed)
        # run if the pokemon is immune
        elif damage == "immune":
            showLabel(immune)
        # run if the effectiveness is super or not very.
        elif effectiveness == "super" or effectiveness == "not very":
            # show the move effectiveness label.
            showLabel(display_effectiveness)
            # take the move damage away from the enemy's health.
            enemy_current_hp -= damage
            if enemy_current_hp <= 0:
                enemy_current_hp = 0
        else:
            # take the move damage away from the enemy's health.
            enemy_current_hp -= damage
            if enemy_current_hp <= 0:
                enemy_current_hp = 0
        # update the enemy health label.
        changeLabel(enemy_hp, f"hp: {round(enemy_current_hp / enemy_stats['health'] * 100, 1)}%")
        if enemy_current_hp == 0:
            battle_won = True
        # play the attacking animation.
        attacking = True
        if attacking is True:
            if starter_choice == "SCEPTILE":
                for i in range(10):
                    changeSpriteImage(sceptile_sprite, 10 + i)
                    pause(80, True)
                attacking = False
            elif starter_choice == "BLAZIKEN":
                for i in range(16):
                    changeSpriteImage(blaziken_sprite, 16 + i)
                    pause(40, True)
                attacking = False
            elif starter_choice == "SWAMPERT":
                for i in range(10):
                    changeSpriteImage(swampert_sprite, i)
                    pause(80, True)
        # stop attacking.
        attacking = False
        # pause before moving on.
        waitPress()
        if enemy_current_hp > 0:
            # hide stuff
            hideLabel(display_move_used)
            hideLabel(display_effectiveness)
            hideLabel(move_missed)
            hideLabel(immune)
            # make the enemy fight back.
            enemy_move_choice = random.randint(0,3)
            damage, effectiveness, punctuation = calc_damage(starter_stats, enemy_moves[enemy_move_choice])
            # make the labels to display the move, it's effectiveness, and if it hit.
            display_move_used = makeLabel(f"{current_enemy} used {enemy_moves[current_move]['name']}!", 40, 30, 290, "white", "Agency FB")
            display_effectiveness = makeLabel(f"It was {effectiveness} effective{punctuation}", 40, 30, 330, "white", "Agency FB")
            move_missed = makeLabel("It missed!", 40, 30, 330, "white", "Agency FB")
            immune = makeLabel("It had no effect.", 40, 30, 330, "white", "Agency FB")
            # show the used move.
            showLabel(display_move_used)
            # run if the move misses.
            if damage == "missed":
                # show the move missed label.
                showLabel(move_missed)
            # run if the pokemon is immune
            elif damage == "immune":
                showLabel(immune)
            # run if the effectiveness is super or not very.
            elif effectiveness == "super" or effectiveness == "not very":
                # show the move effectiveness label.
                showLabel(display_effectiveness)
                # take the move damage away from the player's health.
                player_current_hp -= damage
                if player_current_hp <= 0:
                    player_current_hp = 0
            else:
                # take the move damage away from the player's health.
                player_current_hp -= damage
                if player_current_hp <= 0:
                    player_current_hp= 0
            # update the player health label.
            changeLabel(player_hp, f"hp: {player_current_hp} / {starter_stats['health']}%")
            if player_current_hp == 0:
                battle_lost = True
        # rehide the labels.
        waitPress()
        hideLabel(move_missed)
        hideLabel(immune)
        hideLabel(display_move_used)
        hideLabel(display_effectiveness)
        hide_show_moves("show")
        hideSprite(text_display)
        # re-show the move menus.
        showSprite(battle_menu)
        showLabel(damage_acc)
        showLabel(move_type)
    while battle_won is True:
        # hide the stuff in the way of the menus.
        hide_show_moves("hide")
        hideSprite(battle_menu)
        hideLabel(damage_acc)
        hideLabel(move_type)
        # show the you won text.
        showLabel(text_display)
        showLabel(you_won)
        # wait untill the player presses a button.
        pause(500)
        waitPress()
        # hide some more labels in the way.
        hideLabel(you_won)
        hideLabel(text_display)
        hideLabel(enemy_hp)
        hideLabel(player_hp)
        showSprite(trivia_display)
        hide_show_starter("hide")
        # randomly select a piece of trivia.
        trivia_index = random.randint(0, len(trivia) - 1)
        changeLabel(trivia_label, f"Fun fact:<br>{trivia[trivia_index]}")
        # delete the used trivia so it doesn't appear again.
        del trivia[trivia_index]
        # show the trivia.
        showLabel(trivia_label)
        showSprite(potions)
        pause(100)
        waitPress()
        pause(500)
        # update the current enemy info.
        # switch to lucario if eevee is beaten.
        if current_enemy == 'EEVEE':
            current_enemy = 'LUCARIO'
            enemy_stats = lucario_stats
            hideSprite(eevee_sprite)
            showSprite(lucario_sprite)
            enemy_moves = lucario_moves
            current_trainer = "MILLIE"
            changeLabel(you_won, f"You beat<br>TRAINER {current_trainer}!")
        # switch to garchomp if lucario is beaten.
        elif current_enemy == 'LUCARIO':
            current_enemy = 'GARCHOMP'
            enemy_stats = garchomp_stats
            hideSprite(lucario_sprite)
            showSprite(garchomp_sprite)
            enemy_moves = garchomp_moves
            current_trainer = "MATTHEW"
            changeLabel(you_won, f"You beat<br>TRAINER {current_trainer}!")
        # switch to yveltal if garchomp is beaten.
        elif current_enemy == 'GARCHOMP':
            current_enemy = 'YVELTAL'
            enemy_stats = yveltal_stats
            hideSprite(garchomp_sprite)
            showSprite(yveltal_sprite)
            enemy_moves = yveltal_moves
            current_trainer = "TOBY"
            changeLabel(you_won, f"You beat<br>TRAINER {current_trainer}!")
        # win the game if yveltal is beaten.
        elif current_enemy == 'YVELTAL':
            current_enemy = 'game won'
            enemy_stats = garchomp_stats
            hideSprite(yveltal_sprite)
        # reset the enemy's hp.
        enemy_current_hp = enemy_stats["health"]
        changeLabel(enemy_hp, f"hp: {round(enemy_current_hp / enemy_stats['health'] * 100, 1)}%")
        # hide the trivia labels and sprites.
        # and show the ones for battling.
        hide_show_starter('show')
        hide_show_moves('show')
        showSprite(battle_menu)
        showLabel(move_type)
        showLabel(damage_acc)
        showLabel(enemy_hp)
        showLabel(player_hp)
        hideSprite(potions)
        hideSprite(trivia_display)
        hideLabel(trivia_label)
        # stop the loop
        battle_won = False
endWait()
