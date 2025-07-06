import pygame
import gamesettings as gs

class Game:
  def __init__(self, main, assets):
    self.MAIN = main
    self.ASSETS = assets

  def input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.MAIN.run = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.MAIN.run = False

  def update(self):
    pass

  def draw(self, window):
    pass