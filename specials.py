import pygame
import gamesettings as gc

class Special(pygame.sprite.Sprite):
  def __init__(self, game, image, name, group, row_num, col_num, size):
    super().__init__(group)
    pass

  def update(self):
    pass

  def draw(self, window, x_offset):
    pass

  def bomb_up_special(self, player): 
    pass

  def fire_up_special(self, player):
    pass
  
  def speed_up_special(self, player):
    pass
  
  def wall_hack_special(self, player):
    pass
  
  def remote_special(self, player):
    pass
  
  def bomb_hack_special(self, player):
    pass
  
  def flame_pass_special(self, player):
    pass
  
  def invincible_special(self, player):
    pass
  
  def end_stage(self, player):
    pass
  
  def hit_by_explosion(self):
    pass
  
