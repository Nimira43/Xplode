import pygame
import gamesettings as gs

class Blocks(pygame.sprite.Sprite):
  def __init__(self, game, images, group, row_num, col_num, size):
    pass

  def update(self):
    pass

  def draw(self, window):
    pass

  def __repr__(self):
    pass

class Hard_Block(Blocks):
  def __init__(self, game, images, group, row_num, col_num, size):
    super().__init__(game, images, group, row_num, col_num, size)

class Soft_Block(Blocks):
  def __init__(self, game, images, group, row_num, col_num, size):
    super().__init__(game, images, group, row_num, col_num, size)

  def __repr__(self):
    return "'@'"