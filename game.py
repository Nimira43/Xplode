import pygame
from character import Character
from blocks import Hard_Block, Soft_Block 
from random import choice
import gamesettings as gs

class Game:
  def __init__(self, main, assets):
    self.MAIN = main
    self.ASSETS = assets

    self.groups = {'hard_block': pygame.sprite.Group(),
                   'soft_block': pygame.sprite.Group(),
                   'player': pygame.sprite.Group()}

    self.player = Character(self, self.ASSETS.player_char, self.groups['player'], 3, 2, gs.SIZE)

    self.level = 1
    self.level_matrix = self.generate_level_matrix(gs.ROWS, gs.COLS)

  def input(self):
    self.player.input()

  def update(self):
    for value in self.groups.values():
      for item in value:
        item.update()

  def draw(self, window):
    self.player.draw(window)

  def generate_level_matrix(self, rows, cols):
    matrix = []
    for row in range(rows + 1):
      line = []
      for col in range(cols + 1):
        line.append('_')
      matrix.append(line)
    for row in matrix:
      print(row)
    return matrix