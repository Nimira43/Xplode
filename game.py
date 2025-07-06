import pygame
from character import Character
import gamesettings as gs

class Game:
  def __init__(self, main, assets):
    self.MAIN = main
    self.ASSETS = assets
    self.player = Character(self)

  def input(self):
    self.player.input()

  def update(self):
    pass

  def draw(self, window):
    pass