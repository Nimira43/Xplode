import pygame
import gamesettings as gs

class Character(pygame.sprite.Sprite):
  def __init__(self, game):
    super().__init__()
    self.GAME = game
    self.x = 0
    self.y = 0
    self.alive = True
    self.image = None
    self.rect = pygame.Rect(self.x, self.y, gs.SIZE, gs.SIZE)

  def input(self):
    pass

  def update(self):
    pass

  def draw(self, window):
    pass