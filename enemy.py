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
    self.image = self.image_dict[self.action][self.index]
    self.rect = self.image.get_rect(topleft=(self.x, self.y))

  def update(self):
    self.movement()
    self.animate()

  def draw(self, window, x_offset):
    window.blit(self.image, (self.rect.x - x_offset, self.rect.y))

  def movement(self):
    if self.destroyed:
      return
    move_direction = self.action.split('_')[1]

    if move_direction in ['left', 'right']:
      self.x += self.dir_mvmt[move_direction]
    else:
      self.y += self.dir_mvmt[move_direction]

    directions = ['left', 'right', 'up', 'down']
    self.new_direction(self.GAME.groups['hard_blocks'], move_direction, directions)
    self.new_direction(self.GAME.groups['soft_blocks'], move_direction, directions)
    self.new_direction(self.GAME.groups['bomb'], move_direction, directions)
    self.change_directions(directions)
    self.rect.update(self.x, self.y, self.size, self.size)

  def collision_detection_blocks(self, group, direction):
    for block in group:
      if block.rect.colliderect(self.rect):
        if direction == 'left' and self.rect.right > block.rect.right:
          self.x = block.rect.right
          return direction

  def new_direction(self, group, move_direction, directions):
    pass

  def change_directions(self, direction_list):
    pass

  def determine_if_direction_valid(self, directions, row, col):
    pass

  def animate(self):
    pass

  def destroy(self):
    pass