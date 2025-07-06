import pygame
from assets import Assets
from game import Game
import gamesettings as gs

class Xplode:
  def __init__(self):
    pygame.init()

    self.screen = pygame.display.set_mode((gs.SCREENWIDTH, gs.SCREENHEIGHT))
    pygame.display.set_caption('Xplode')

    self.ASSETS = Assets()
    self.FPS = pygame.time.Clock()
    self.run = True

  def input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.run = False

  def update(self):
    self.FPS.tick(gs.FPS)

  def draw(self, window):
    window.fill(gs.BLACK)
    pygame.display.update()

  def rungame(self):
    while self.run == True:
      self.input()
      self.update()
      self.draw(self.screen)

if __name__ == '__main__':
  game = Xplode()
  game.rungame()
  pygame.quit()