import pygame
import gamesettings as gs

class Xplode:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((gs.SCREENWIDTH, gs.SCREENHEIGHT))
    pygame.display.set_caption('Xplode')
    self.FPS = pygame.time.Clock()
    self.run = True

  def input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.run = False

  def update(self):
    pass

  def draw(self, window):
    pass

  def rungame(self):
    pass

if __name__ == '__main__':
  game = Xplode()
  game.rungame()
  pygame.quit()