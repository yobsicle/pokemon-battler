import pygame
from pygame_functions import *
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

eevee_moves = ({"name": "TACKLE", "damage": 40, "accuracy": 100, "type": "NORMAL", "stab": True},
               {"name": "TAKE DOWN", "damage": 90, "accuracy": 85, "type": "NORMAL", "stab": True},
               {"name": "SPLASH", "damage": 0, "accuracy": 100, "type": "NORMAL", "stab": True},
               {"name": "DOUBLE KICK", "damage": 60, "accuracy": 100, "type": "FIGHTING", "stab": False})

garchomp_moves = ({"name": "BITE", "damage": 60, "accuracy": 100, "type": "DARK", "stab": False},
                  {"name": "TAKE DOWN", "damage": 90, "accuracy": 85, "type": "NORMAL", "stab": False},
                  {"name": "DRAGON TAIL", "damage": 60, "accuracy": 90, "type": "DRAGON", "stab": True},
                  {"name": "TACKLE", "damage": 40, "accuracy": 100, "type": "NORMAL", "stab": False})

lucario_moves = ({"name": "METAL CLAW", "damage": 50, "accuracy": 95, "type": "STEEL", "stab": True},
                 {"name": "ROCK SMASH", "damage": 40, "accuracy": 100, "type": "FIGHTING", "stab": True},
                 {"name": "FORCE PALM", "damage": 60, "accuracy": 100, "type": "FIGHTING", "stab": True},
                 {"name": "TRAILBLAZE", "damage": 50, "accuracy": 100, "type": "GRASS", "stab": False})

yveltal_moves = ({"name": "OBLIVION WING", "damage": 80, "accuracy": 100, "type": "FLYING", "stab": True},
                 {"name": "DRAGON RUSH", "damage": 100, "accuracy": 75, "type": "DRAGON", "stab": False},
                 {"name": "HURRICANE", "damage": 110, "accuracy": 70, "type": "FLYING", "stab": True},
                 {"name": "PSYCHIC", "damage": 90, "accuracy": 100, "type": "PSYCHIC", "stab": False})

