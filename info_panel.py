import pygame
import gamesettings as gs

class InfoPanel:
  def __init__(self, game, images):
    self.GAME = game
    self.images = images
    self.black_nums = self.images.numbers_block
    self.set_timer()
    self.player_lives_left_word = self.images.left_word
    self.score_image = self.update_score_image(self.GAME.player.score)

  def set_timer(self):
    self.time_total = gs.STAGE_TIME
    self.timer_start = pygame.time.get_ticks()
    self.time = 200
    self.time_image = self.update_time_image()
    self.time_word_image = self.images.time_word
    self.time_word_rect = self.time_word_image.get_rect(topleft=(32, 32))

  def update_time_image(self):
    num_string_list = [item for item in str(self.time)]
    images = [self.black_nums[int(image)][0] for image in num_string_list]
    return images

  def update(self):
    self.score_image = self.update_score_image(self.GAME.player.score)

    if self.time == 0:
      return
    
    if pygame.time.get_ticks() - self.timer_start >= 1000:
      self.timer_start = pygame.time.get_ticks()
      self.time -= 1
      self.time_image = self.update_time_image()
      if self.time == 0:
        self.GAME.insert_enemies_into_level(self.GAME.level_matrix, ['pontan' for _ in range(10)])

  def draw(self, window):
    window.blit(self.time_word_image, self.time_word_rect)
    
    start_x = 192 if len(self.time_image) == 3 else 224 if len(self.time_image) == 2 else 256
    for num, image in enumerate(self.time_image):
      window.blit(image, (start_x + (32 * num), 32))
    
    start_x = ((gs.SCREENWIDTH // 2) + 64 ) - (len(self.score_image) * 32)
    for num, image in enumerate(self.score_image):
      window.blit(image, (start_x + (32 * num), 32))

    window.blit(self.player_lives_left_word, (1032, 32))
    window.blit(self.black_nums[self.GAME.player.lives][0], (1184, 32))

  def update_score_image(self, score):
    if score == 0:
      score_images = [self.black_nums[0][0], self.black_nums[0][0]]
    else:
      score_images = [self.black_nums[int(digit)][0] for digit in str(score)]
    return score_images

class Scoring():
  scoring_bonus = 0

  def __init__(self, game, group, score, xpos, ypos):
    super().__init__(group)
    Scoring.score_bonus += 1

    self.GAME = game
    self.score = score if Scoring.score_bonus <= 1 else score * 2  

  def update(self):
    pass

  def draw(self, window, x_offset):
    pass

