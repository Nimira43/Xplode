import pygame
import gamesettings as gs
from random import choice

class Enemy(pygame.sprite.Sprite):
  def __init__(self, game, image_dict, group, type, row_num, col_num, size):
    super().__init__(group)
    self.GAME = game
    self.type = type
    self.speed = gs.ENEMIES[self.type]['speed']
    self.wall_hack = gs.ENEMIES[self.type]['wall_hack']
    self.chase_player = gs.ENEMIES[self.type]['chase_player']
    self.LoS = gs.ENEMIES[self.type]['LoS'] * size
    self.see_player_hack = gs.ENEMIES[self.type]['see_player_hack']
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
    self.start_pos = self.rect.center
    self.end_pos = self.GAME.player.rect_center

  def update(self):
    self.movement()
    self.update_line_of_sight_with_player()
    self.animate()

  def draw(self, window, x_offset):
    window.blit(self.image, (self.rect.x - x_offset, self.rect.y))
    pygame.draw.line(window, 'black', (self.start_pos[0] - x_offset, self.start_pos[1]), (self.end_pos[0] - x_offset, self.end_pos[1]), 2)

  def movement(self):
    if self.destroyed:
      return
    move_direction = self.action.split('_')[1]

    if move_direction in ['left', 'right']:
      self.x += self.dir_mvmt[move_direction]
    else:
      self.y += self.dir_mvmt[move_direction]

    directions = ['left', 'right', 'up', 'down']
    self.new_direction(self.GAME.groups['hard_block'], move_direction, directions)
    self.new_direction(self.GAME.groups['soft_block'], move_direction, directions)
    self.new_direction(self.GAME.groups['bomb'], move_direction, directions)
    self.change_directions(directions)
    self.rect.update(self.x, self.y, self.size, self.size)

  def collision_detection_blocks(self, group, direction):
    for block in group:
      if block.rect.colliderect(self.rect):
        if direction == 'left' and self.rect.right > block.rect.right:
          self.x = block.rect.right
          return direction
        if direction == 'right' and self.rect.left < block.rect.left:
          self.x = block.rect.left - self.size
          return direction
        if direction == 'up' and self.rect.bottom > block.rect.bottom:
          self.y = block.rect.bottom
          return direction
        if direction == 'down' and self.rect.top < block.rect.top:
          self.y = block.rect.top - self.size
          return direction
    return None  

  def new_direction(self, group, move_direction, directions):
    dir = self.collision_detection_blocks(group, move_direction)
    if dir:
      directions.remove(dir)
      new_direction = choice(directions)
      self.action = f'walk_{new_direction}'
      self.change_dir_timer = pygame.time.get_ticks()

  def change_directions(self, direction_list):
    if pygame.time.get_ticks() - self.change_dir_timer < self.dir_time:
      return
    
    if self.x % self.size != 0 or (self.y - gs.Y_OFFSET) % self.size != 0:
      return
    
    row = int((self.y - gs.Y_OFFSET) // self.size)
    col = int(self.x // self.size)

    if row % 2 == 0 or col % 2 == 0:
      return
    
    self.determine_if_direction_valid(direction_list, row, col)

    new_direction = choice(direction_list)
    self.action = f'walk_{new_direction}'

    self.change_dir_timer = pygame.time.get_ticks()
    return

  def determine_if_direction_valid(self, directions, row, col):
    if self.GAME.level_matrix[row - 1][col] != '_':
      directions.remove('up')
    if self.GAME.level_matrix[row + 1][col] != '_':
      directions.remove('down')
    if self.GAME.level_matrix[row][col - 1] != '_':
      directions.remove('left')
    if self.GAME.level_matrix[row][col + 1] != '_':
      directions.remove('right')
    if len(directions) == 0:
      directions.append('left')
    return
    
  def animate(self):
    if pygame.time.get_ticks() - self.anim_timer >= self.anim_frame_time:
      self.index += 1
      if self.destroyed and self.index == len(self.image_dict[self.action]):
        self.kill()
      self.index = self.index % len(self.image_dict[self.action])
      self.image = self.image_dict[self.action][self.index]
      self.anim_timer = pygame.time.get_ticks()
     
  def destroy(self):
    self.destroyed = True
    self.index = 0
    self.action = 'death'
    self.image = self.image_dict[self.action][self.index]

  def update_line_of_sight_with_player(self):
    pass

  def chase_the_player(self):
    pass

  def check_LoS_distance(self):
    pass

  def intersecting_items_with_Los(self, group):
    pass
  