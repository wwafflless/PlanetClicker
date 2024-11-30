import pygame

pygame.init()
import pytest
from planetclicker.data import Game
from planetclicker.sprite.animated_sprite import AnimatedSprite
from planetclicker.sprite.sprite_sheet import SpriteSheet
from pygame.sprite import Sprite


@pytest.mark.skip
def test_sheet():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    sprite_sheet = SpriteSheet("asset/sheet/orb_2.png")
    image_0 = sprite_sheet.image_at((0, 0, 51, 51))
    rect = image_0.get_rect()
    image_strip = sprite_sheet.load_strip(rect, 10, (0, 0, 51, 51))
    rect = image_0.get_rect()
    rect.topleft = (0, 0)
    while True:
        screen.fill(Game.Color.black, (0, 0, 400, 300))
        for img in image_strip:
            screen.blit(img, rect)
        pygame.display.flip()


def test_animated_sprite():
    screen = pygame.display.set_mode((400, 300))
    sprite = AnimatedSprite(
        name="asset/sheet/orb_2.png",
        w=51,
        h=51,
        frames=10,
    )
    hi_txt = Game.Font.title.render("HELLO", False, Game.Color.white)
    while True:
        screen.fill(Game.Color.background, (0, 0, 400, 300))
        sprite.update()
        screen.blit(sprite.current_image, sprite.current_rect)
        screen.blit(hi_txt, screen.get_rect().center)
        pygame.display.flip()


@pytest.mark.skip
def test_custom_sprite():
    class CustomSprite(Sprite):
        def __init__(self, *groups: pygame.sprite.Group) -> None:
            super().__init__(*groups)
            self.image = pygame.image.load("asset/sprite/sun.png")

        def update(self) -> None:
            return super().update()

        def draw(self, surface):
            surface.blit(self.image, (0, 0))

    s = CustomSprite()
    screen = pygame.display.set_mode((400, 300))
    screen.fill(Game.Color.black, (0, 0, 400, 300))
    while True:
        s.draw(screen)
        pygame.display.flip()
