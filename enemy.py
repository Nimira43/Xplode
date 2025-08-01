import pygame
import gamesettings as gs
from random import choice

class Enemy(pygame.sprite.Sprite):
  def __init__(self, game, image_dict, group, row_num, col_num, size):
    super().__init__(group)
    self.GAME = game
    self.speed = 1
    self.wall_hack = False
    self.chase_player = False
    self.LoS = 0
    self.see_player_hack = False
    self.row = row_num
    self.col = col_num
    self.size = size
    self.x = self.col * self.size
    self.y = (self.row * self.size) + gs.Y_OFFSET
    self.destroyed = False
    self.direction = 'left'
    self.dir_mvmt = {'left': -self.speed, 'right': self.speed, 'up': -self.speed, 'down': self.speed}

    self.change_dir_timer = pygame.time.get_ticks()
    self.dir_time = 1500
    self.index = 0
    self.action = f'walk_{self.direction}'
    self.image_dict = image_dict
    self.anim_frame_time = 100
    self.anim_timer = pygame.time.get_ticks()

  def update(self):
    pass

  def draw(self, window, x_offset):
    pass

  def movement(self):
    pass

  def collision_detection_blocks(self, group, direction):
    pass

  def new_direction(self, group, move_direction, directions):
    pass

  def change_direction(self, direction_list):
    pass

  def determine_if_direction_valid(self, directions, row, col):
    pass

  def animate(self):
    pass

  def destroy(self):
    pass