import pygame
import gamesettings as gs

class Assets:
  def __init__(self):
    self.spritesheet = self.load_sprite_sheet('image', 'spritesheet.png', 192 * 4, 272 * 4)

    self.player_char = self.load_sprite_range(gs.PLAYER, self.spritesheet)

  def load_sprite_sheet(self, path, filename, width, height):
    image = pygame.image.load(f'{path}/{filename}').convert_alpha()
    image = pygame.transform.scale(image, (width, height))
    return image
  
  def load_sprites(self, spritesheet, xcoord, ycoord, width, height):
    pass