import pygame
from character import Character
from enemy import Enemy
from blocks import Hard_Block, Soft_Block, Special_Soft_Block 
from random import choice, randint
import gamesettings as gs

class Game:
  def __init__(self, main, assets):
    self.MAIN = main
    self.ASSETS = assets
    self.camera_x_offset = 0

    self.groups = {'hard_block': pygame.sprite.Group(),
                   'soft_block': pygame.sprite.Group(),
                   'bomb': pygame.sprite.Group(),
                   'specials': pygame.sprite.Group(),
                   'explosions': pygame.sprite.Group(),
                   'enemies': pygame.sprite.Group(),
                   'player': pygame.sprite.Group()}

    self.player = Character(self, self.ASSETS.player_char, self.groups['player'], 3, 2, gs.SIZE)

    self.level = 1
    self.level_special = self.select_a_special()
    self.level_matrix = self.generate_level_matrix(gs.ROWS, gs.COLS)

  def input(self):
    self.player.input()

  def update(self):
    for value in self.groups.values():
      for item in value:
        item.update()

    if self.groups['explosions']:
      killed_enemies = pygame.sprite.groupcollide(self.groups['explosions'], self.groups['enemies'], False, False)
      if killed_enemies:
        for flame, enemies in killed_enemies.items():
          for enemy in enemies:
            if pygame.sprite.collide_mask(flame, enemy):
              enemy.destroy()

  def draw(self, window):
    window.fill(gs.GREY)

    for row_num, row in enumerate(self.level_matrix):
      for col_num, col in enumerate(row):
        window.blit(self.ASSETS.background['background'][0],
                    ((col_num * gs.SIZE) -self.camera_x_offset, (row_num * gs.SIZE) + gs.Y_OFFSET))
    
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
    self.insert_power_up_into_matrix(matrix, self.level_special)
    self.insert_power_up_into_matrix(matrix, 'exit')
    self.insert_enemies_into_level(matrix)
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

  def insert_power_up_into_matrix(self, matrix, special):
    power_up = special
    valid = False
    

  def update_x_camera_offset_player_position(self, player_x_pos):
    if player_x_pos >= 576 and player_x_pos <= 1280:
      self.camera_x_offset = player_x_pos - 576    

  def insert_enemies_into_level(self, matrix): 
    enemies_list = ['bollom' for i in range(10)]
    pl_col = self.player.col_num
    pl_row = self.player.row_num

    for enemy in enemies_list:
      valid_choice = False
      while not valid_choice:
        row = randint(0, gs.ROWS)
        col = randint(0, gs.COLS)

        if row in [pl_row - 3, pl_row - 2, pl_row - 1, pl_row, pl_row + 1, pl_row + 2, pl_row + 3] and \
        col in [pl_col - 3, pl_col - 2, pl_col - 1, pl_col, pl_col + 1, pl_col + 2, pl_col + 3]:
          continue

        elif matrix[row][col] == '_':
          valid_choice = True
          Enemy(self, self.ASSETS.ballom, self.groups['enemies'], row, col, gs.SIZE)
        else:
          continue