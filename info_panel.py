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

  def update_time_image(self):
    pass

  def update(self):
    pass

  def draw(self, window):
    pass

  def update_score_image(self, score):
    pass

class Scoring():
  def __init__(self, game, group, score, xpos, ypos):
    pass  

  def update(self):
    pass

  def draw(self, window, x_offset):
    pass

