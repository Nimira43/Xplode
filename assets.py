import pygame
import gamesettings as gs

class Assets:
  def __init__(self):
    self.spritesheet = self.load_sprite_sheet('image', 'spritesheet.png', 192 * 4, 272 * 4)