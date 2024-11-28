import os

import pygame
from pygame.surface import Surface


def load_sprite(path) -> Surface:
    return pygame.image.load(os.path.join("asset", "sprite", path + ".png"))


# class Sprite(pygame.sprite.Sprite):
#     @classmethod
#     def from_image_name(cls, name):
#         sprite_image = load_sprite(name)
#         sprite = cls(sprite_image)
#         sprite.rect = sprite_image.get_rect()
#         return sprite
