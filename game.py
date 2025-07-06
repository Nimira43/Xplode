import pygame
from character import Character
from blocks import Hard_Block, Soft_Block 
from random import choice
import gamesettings as gs

class Game:
  def __init__(self, main, assets):
    self.MAIN = main
    self.ASSETS = assets
    self.player = Character(self, self.ASSETS.player_char)

    self.level = 1
    self.level_matrix = self.generate_level_matrix(gs.ROWS, gs.COLS)

  def input(self):
    self.player.input()

  def update(self):
    self.player.update()

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