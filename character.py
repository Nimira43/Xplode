import pygame
import gamesettings as gs

class Character(pygame.sprite.Sprite):
  def __init__(self, game):
    super().__init__()
    self.GAME = game

  def input(self):
    pass

  def update(self):
    pass

  def draw(self, window):
    pass