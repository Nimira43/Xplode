import pygame
from character import Character
from blocks import Hard_Block, Soft_Block 
from random import choice
import gamesettings as gs

class Game:
  def __init__(self, main, assets):
    self.MAIN = main
    self.ASSETS = assets
    self.camera_x_offset = 0

    self.groups = {'hard_block': pygame.sprite.Group(),
                   'soft_block': pygame.sprite.Group(),
                   "bomb": pygame.sprite.Group(),
                   "explosions": pygame.sprite.Group(),
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
    window.fill(gs.GREY)

    for row_num, row in enumerate(self.level_matrix):
      for col_num, col in enumerate(row):
        window.blit(self.ASSETS.background['background'][0],
                    ((col_num * gs.SIZE), (row_num * gs.SIZE) + gs.Y_OFFSET))
    
    for value in self.groups.values():
      for item in value:
        item.draw(window, self.camera_x_offset)

  def generate_level_matrix(self, rows, cols):
    matrix = []
    for row in range(rows + 1):
      line = []
      for col in range(cols + 1):
        line.append('_')
      matrix.append(line)
    self.insert_hard_blocks_into_matrix(matrix)
    self.insert_soft_blocks_into_matrix(matrix)
    for row in matrix:
      print(row)
    return matrix
  
  def insert_hard_blocks_into_matrix(self, matrix):
    for row_num, row in enumerate(matrix):
      for col_num, col in enumerate(row):
        if row_num == 0 or row_num == len(matrix)-1 or \
          col_num == 0 or col_num == len(row)-1 or \
            (row_num % 2 == 0 and col_num % 2 == 0):
          matrix[row_num][col_num] = Hard_Block(self, self.ASSETS.hard_block['hard_block'], 
                                                self.groups['hard_block'], row_num, col_num, gs.SIZE)
    return 

  
  def insert_soft_blocks_into_matrix(self, matrix):
    for row_num, row in enumerate(matrix):
      for col_num, col in enumerate(row):
        if row_num == 0 or row_num == len(matrix)-1 or \
          col_num == 0 or col_num == len(row)-1 or \
            (row_num % 2 == 0 and col_num % 2 == 0):
          continue
        elif row_num in [2, 3, 4] and col_num in [1, 2, 3]:
          continue
        else:
          cell = choice(['@', '_', '_', '_'])
          if cell == '@':
            cell = Soft_Block(self, self.ASSETS.soft_block['soft_block'],
                              self.groups['soft_block'], row_num, col_num, gs.SIZE)
          matrix[row_num][col_num] = cell
    return      

  def update_x_camera_offset_player_position(self, player_x_pos):
    if player_x_pos >= 576 and player_x_pos <= 1280:
      self.camera_x_offset = player_x_pos - 576    

