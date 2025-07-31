import pygame
import gamesettings as gs
from random import choice

class Enemy(pygame.sprite.Sprite):
  def __init__(self, game, image_dict, group, row_num, col_num, size):
    pass

  def update(self):
    pass

  def draw(self, window, x_offset):
    pass

  def movement(self):
    pass

  def collision_detection_blocks(self, group, direction):
    pass

  def new_direction(self, group, move_direction, directions):
    pass

  def change_direction(self, direction_list):
    pass

  def determine_if_direction_valid(self, directions, row, col):
    pass

  def animate(self):
    pass

  def destroy(self):
    pass