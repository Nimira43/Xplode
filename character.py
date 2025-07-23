import pygame
import gamesettings as gs

class Character(pygame.sprite.Sprite):
  def __init__(self, game, image_dict, group, row_num, col_num, size):
    super().__init__(group)
    self.GAME = game
    self.row_num = row_num
    self.col_num = col_num
    self.size = size
    self.x = self.col_num * self.size
    self.y = (self.row_num * self.size) + gs.Y_OFFSET
    self.alive = True
    self.speed = 3
    self.bomb_limit = 2
    self.remote = True
    self.power = 2
    self.action = 'walk_left'
    self.bombs_planted = 0
    self.index = 0
    self.anim_time = 50
    self.anim_time_set = pygame.time.get_ticks()
    self.image_dict = image_dict
    self.image = self.image_dict[self.action][self.index]
    self.rect = self.image.get_rect(topleft=(self.x, self.y))

  def input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.GAME.MAIN.run = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.GAME.MAIN.run = False
        elif event.key == pygame.K_SPACE:
          row, col = ((self.rect.centery - gs.Y_OFFSET) // gs.SIZE, self.rect.centerx // self.size)
          if self.GAME.level_matrix[row][col] == '_' and self.bombs_planted < self.bomb_limit: 
            Bomb(self.GAME, self.GAME.ASSETS.bomb['bomb'], self.GAME.groups['bomb'], self.power, row, col, gs.SIZE, self.remote)
        elif event.key == pygame.K_LCTRL and self.remote and self.GAME.groups['bomb']:
          bomb_list = self.GAME.groups['bomb'].sprites()
          bomb_list[-1].explode()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
      self.move('walk_right')
    elif keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
      self.move('walk_left')
    elif keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
      self.move('walk_up')
    elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
      self.move('walk_down')

  def update(self):
    pass

  def draw(self, window, offset):
    window.blit(self.image, (self.rect.x - offset, self.rect.y))
    pygame.draw.rect(window, gs.RED, (self.rect.x - offset, self.rect.y, 64, 64), 1)

  def animate(self, action):
    if pygame.time.get_ticks() - self.anim_time_set >= self.anim_time:
      self.index += 1
      if self.index == len(self.image_dict[action]):
        self.index = 0

      self.image = self.image_dict[action][self.index]
      self.anim_time_set = pygame.time.get_ticks()

  def move(self, action):
    if not self.alive:
      return
    
    if action != self.action:
      self.action = action
      self.index = 0

    direction = {'walk_left': -self.speed, 'walk_right': self.speed, 'walk_up': -self.speed, 'walk_down': self.speed}

    if action == 'walk_left' or action == 'walk_right':
      self.x += direction[action]
    elif action == 'walk_up' or action == 'walk_down':
      self.y += direction[action]

    self.animate(action)
    self.snap_to_grid(action)
    self.play_area_restriction(64, (gs.COLS - 1) * 64, gs.Y_OFFSET + 64, ((gs.ROWS - 1) * 64) + gs.Y_OFFSET)
    self.rect.topleft = (self.x, self.y)

    self.collision_detection_items(self.GAME.groups['hard_block'])
    self.collision_detection_items(self.GAME.groups['soft_block'])

    self.GAME.update_x_camera_offset_player_position(self.rect.x)

  def collision_detection_items(self, item_list):
    for item in item_list:
      if self.rect.colliderect(item) and item.passable == False:
        if self.action == 'walk_right':
          if self.rect.right > item.rect.left:
            self.rect.right = item.rect.left
            self.x, self.y = self.rect.topleft
            return
        if self.action == 'walk_left':
          if self.rect.left < item.rect.right:
            self.rect.left = item.rect.right
            self.x, self.y = self.rect.topleft
            return
        if self.action == 'walk_up':
          if self.rect.top < item.rect.bottom:
            self.rect.top = item.rect.bottom
            self.x, self.y = self.rect.topleft
            return
        if self.action == 'walk_down':
          if self.rect.bottom > item.rect.top:
            self.rect.bottom = item.rect.top
            self.x, self.y = self.rect.topleft
            return
          
  def snap_to_grid(self, action):
    x_pos = self.x % gs.SIZE
    y_pos = (self.y - gs.Y_OFFSET) % gs.SIZE

    if action in ['walk_up', 'walk_down']:
      if x_pos <= 12:
        self.x = self.x - x_pos
      if x_pos >= 52:
        self.x = self.x + (gs.SIZE - x_pos)
    
    elif action in ['walk_left', 'walk_right']:
      if y_pos <= 12:
        self.y = self.y - y_pos
      if y_pos >= 52:
        self.y = self.y + (gs.SIZE - y_pos)


  def play_area_restriction(self, left_x, right_x, top_y, bottom_y):
    if self.x < left_x:
      self.x = left_x
    elif self.x > right_x:
      self.x = right_x
    elif self.y < top_y:
      self.y = top_y
    elif self.y > bottom_y:
      self.y = bottom_y

class Bomb(pygame.sprite.Sprite):
  def __init__(self, game, image_list, group, power, row_num, col_num, size, remote):
    super().__init__(group)
    self.GAME = game
    self.row = row_num
    self.col = col_num
    self.size = size
    self.x = self.col * self.size
    self.y = (self.row * self.size) + gs.Y_OFFSET

    self.bomb_counter = 1
    self.bomb_timer = 12
    self.passable = True
    self.remote = remote
    self.power = power

    self.index = 0
    self.image_list = image_list
    self.image = self.image_list[self.index]
    self.rect = self.image.get_Rect(topleft=(self.x, self.y))

    self.anim_length = len(self.image_list)
    self.anim_frame_time = 200
    self.anim_timer = pygame.time.get_ticks()
    self.insert_bomb_into_grid()

  def update(self):
    self.animation()
    self.planted_bomb_player_collision()
    if self.bomb_counter == self.bomb_timer and not self.remote:
      self.explode()

  def draw(self, window, offset):
    window.blit(self.image, (self.rect.x - offset, self.rect.y))

  def insert_bomb_into_grid(self):
    self.GAME.level_matrix[self.row][self.col] = self
    self.GAME.player.bombs_planted += 1

  def animation(self):
    if pygame.time.get_ticks() - self.anim_timer >= self.anim_frame_time:
      self.index += 1
      self.index = self.index % self.anim_length
      self.image = self.image_list[self.index]
      self.anim_timer = pygame.time.get_ticks()
      self.bomb_counter += 1

  def remove_bomb_from_grid(self):
    self.GAME.level_matrix[self.row][self.col] = "_"
    self.GAME.player.bombs_pplanted -= 1

  def explode(self):
    self.kill()
    Explosion(self.GAME, self.GAME.ASSETS.explosions, 'centre', self.power, self.GAME.groups['explosions'], self.row, self.col, self.size)
    self.remove_bomb_from_grid()

  def planted_bomb_player_collision(self):
    if not self.passable:
      return
    if not self.rect.colliderect(self.GAME.player):
      self.passable = False

  def __repr__(self):
    return "'!'"
  
class Explosion(pygame.sprite.Sprite):
  def __init__(self, game, image_dict, image_type, power, group, row_num, col_num, size):
    super().__init__(group)
    self.GAME = game
    self.row_num = row_num
    self.col_num = col_num
    self.size = size
    self.y = (self.row_num * self.size) + gs.Y_OFFSET
    self.x = self.col_num * self.size
    self.index = 0
    self.anim_frame_time = 75
    self.anim_timer = pygame.time.get_ticks()
    self.image_dict = image_dict
    self.image_type = image_type
    self.image = self.image_dict[self.image_type][self.index]
    self.rect = self.image.get_rect(topleft=(self.x, self.y))
    self.power = power
    self.passable = False
    self.calculate_explosive_path()

  def update(self):
    self.animate()

  def draw(self, window, x_offset):
    window.blit(self.image, (self.rect.x - x_offset, self.rect.y))

  def animate(self): 
    if pygame.time.get_ticks() - self.anim_timer >= self.anim_frame_time:
      self.index += 1
      if self.index == len(self.image_dict[self.image_type]):
        self.kill()
        return
      self.image = self.image_dict[self.image_type][self.index]
      self.anim_timer = pygame.time.get_ticks()

  def calculate_explosive_path(self):
    valid_directions = [True, True, True, True]
    for power_cell in range(self.power):
      directions = self.calculate_direction_cells(power_cell)
      for ind, dir in enumerate(directions):
        if not valid_directions[ind]:
          continue
        if self.GAME.level_matrix[dir[0]][dir[1]] == '_':
          if power_cell == self.power - 1:
            FireBall(self.image_dict[dir[4], self.GAME.groups['explosions'], dir[0], dir[1], gs.SIZE])
          elif self.GAME.level_matrix[dir[2]][dir[3]] in self.GAME.groups['hard_block'].sprites():
            FireBall(self.image_dict[dir[4]], self.GAME.groups['explosions'], dir[0], dir[1], gs.SIZE)
            valid_directions[ind] = False
          else:
            FireBall(self.image_dict[dir[5]], self.GAME.groups['explosions'], dir[0], dir[1], gs.SIZE)
        elif self.GAME.level_matrix[dir[0]][dir[1]] in self.GAME.groups['bomb'].sprites():
          self.GAME.level_matrix[dir[0]][dir[1]].explode()
          valid_directions[ind] = False
        elif self.GAME.level_matrix[dir[0]][dir[1]] in self.GAME.groups['soft_block'].sprites():
          self.GAME.level_matrix[dir[0]][dir[1]].destroy_soft_blocks()
          valid_directions[ind] = False
        else:
          valid_directions[ind] = False
          continue
        

  def calculate_direction_cells(self, cell):
    left = (self.row_num, self.col_num - (cell + 1),
            self.row_num, self.col_num - (cell + 2),
            'left_end', 'left_mid' )
    right = (self.row_num, self.col_num + (cell + 1),
            self.row_num, self.col_num + (cell + 2),
            'right_end', 'right_mid' )
    up = (self.row_num - (cell + 1), self.col_num,
            self.row_num - (cell + 2), self.col_num,
            'up_end', 'up_mid' )
    down = (self.row_num + (cell + 1), self.col_num,
            self.row_num + (cell + 2), self.col_num,
            'down_end', 'down_mid' )
    return [left, right, up, down]
    

class FireBall(pygame.sprite.Sprite):
  def __init__(self, image_list, group, row_num, col_num, size):
    super().__init__(group)
    self.row_num = row_num
    self.col_num = col_num
    self.size = size
    self.y = self.row_num * self.size + gs.Y_OFFSET
    self.x = self.col_num * self.size
    self.index = 0
    self.anim_frame_time = 75
    self.anim_timer = pygame.time.get_ticks()
    self.image_list = image_list
    self.image = self.image_list[self.index]
    self.rect = self.image.get_rect(topleft=(self.x, self.y))
    self.passable = False

  def update(self):
    self.animate()

  def draw(self, window, x_offset):
    pass

  def animate(self): 
    pass

 
