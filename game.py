import pygame
from character import Character
import gamesettings as gs

class Game:
  def __init__(self, main, assets):
    self.MAIN = main
    self.ASSETS = assets
    self.player = Character(self, self.ASSETS, player_char)

  def input(self):
    self.player.input()

  def update(self):
    self.player.update()

  def draw(self, window):
    self.player.draw(window)