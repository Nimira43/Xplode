import pygame
import gamesettings as gs

class Assets:
  def __init__(self):
    self.spritesheet = self.load_sprite_sheet('images', 'spritesheet.png', 192 * 4, 272 * 4)

    self.player_char = self.load_sprite_range(gs.PLAYER, self.spritesheet)
    self.hard_block = self.load_sprite_range(gs.HARD_BLOCK, self.spritesheet)
    self.soft_block = self.load_sprite_range(gs.SOFT_BLOCK, self.spritesheet)
    self.background = self.load_sprite_range(gs.BACKGROUND, self.spritesheet)
    self.bomb = self.load_sprite_range(gs.BOMB, self.spritesheet)
    self.explosions = self.load_sprite_range(gs.EXPLOSIONS, self.spritesheet)

    for image_list in ['right_end', 'right_mid', 'down_end', 'down_mid']:
      self.rotate_images_in_list(self.explosions[image_list], 180)

  def load_sprite_sheet(self, path, filename, width, height):
    image = pygame.image.load(f"{path}/{filename}").convert_alpha()
    image = pygame.transform.scale(image, (width, height))
    return image
  
  def load_sprites(self, spritesheet, xcoord, ycoord, width, height):
    image = pygame.Surface((width, height))
    image.fill((0, 0, 1))
    image.blit(spritesheet, (0, 0), (xcoord, ycoord, width, height))
    image.set_colorkey(gs.BLACK)
    return image

  def load_sprite_range(self, image_dict, spritesheet, row=gs.SIZE, col=gs.SIZE, width=gs.SIZE, height=gs.SIZE, resize=False):
    animation_images = {}
    for animation in image_dict.keys():
      animation_images[animation] = []
      for coord in image_dict[animation]:
        image = self.load_sprites(spritesheet, coord[1] * col, coord[0] * row, width, height)
        if resize:
          image = pygame.transform.scale(image, (32, 32))
        animation_images[animation].append(image)
    return animation_images
  
  def rotate_images_in_list(self, image_list, rotation):
    for ind, image in enumerate(image_list):
      image = pygame.transform.rotate(image, rotation)
      image_list[ind] = image