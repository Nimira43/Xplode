import pygame
import gamesettings as gs

class Character(pygame.sprite.Sprite):
  def __init__(self, game):
    super().__init__()
    self.GAME = game
    self.x = 0
    self.y = 0
    self.alive = True
    self.speed = 3
    self.image = None
    self.rect = pygame.Rect(self.x, self.y, gs.SIZE, gs.SIZE)

  def input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.GAME.MAIN.run = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.GAME.MAIN.run = False

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
      self.x += self.speed
    elif keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
      self.x -= self.speed
    elif keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
      self.y -= self.speed
    elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
      self.y += self.speed

  def update(self):
    pass

  def draw(self, window):
    pygame.draw.rect(window, gs.RED, self.rect)