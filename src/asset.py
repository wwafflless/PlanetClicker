import pygame
import os

# print current working directory
f = os.path.join(os.getcwd(), "assets", "ThaleahFat.ttf")
print(f)

pixel_font = pygame.font.Font(f, 16)

planet_images = dict(
    earth=pygame.image.load("assets/earth.png"),
    moon=pygame.image.load("assets/moon.png"),
    mercury=pygame.image.load("assets/mercury.png"),
    venus=pygame.image.load("assets/venus.png"),
    sun=pygame.image.load("assets/sun.png"),
    mars=pygame.image.load("assets/mars.png"),
    saturn=pygame.image.load("assets/saturn.png"),
    jupiter=pygame.image.load("assets/jupiter.png"),
)
