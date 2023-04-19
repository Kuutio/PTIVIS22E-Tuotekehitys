from pygame.locals import *
import pygame
from typing import Sequence

from common import Vector2

from player import Player

import settings


def movement_direction(pressed_keys: Sequence[bool]) -> Vector2:
    direction = Vector2(0,0)
    
    if pressed_keys[K_w]:
        direction.y -= 1
    if pressed_keys[K_s]:
        direction.y += 1
    if pressed_keys[K_d]:
        direction.x += 1
    if pressed_keys[K_a]:
        direction.x -= 1


    if direction.length() != 0:
        direction.normalize_ip()
        
    return direction

def get_mouse_position_relative(center) -> Vector2:
        # calculate where the mouse is on the canvas relative to the player
        # based on where it is relative to the centre of the screen
    display_centre_x = settings.display["width"] / 2
    display_centre_y = settings.display["height"] / 2
    display_centre = Vector2(display_centre_x, display_centre_y)

    mouse_pos = Vector2(pygame.mouse.get_pos())
    mouse_rel_to_centre = display_centre - mouse_pos
    mouse_rel_to_player = center - mouse_rel_to_centre
    return mouse_rel_to_player
