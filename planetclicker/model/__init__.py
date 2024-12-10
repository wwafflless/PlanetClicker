import pygame


class BlankSprite(pygame.sprite.Sprite):
    def __init__(self, *groups: pygame.sprite.Group) -> None:
        super().__init__(*groups)
        self.image = pygame.image.load("assets/sprite/blank.png")

    def update(self) -> None:
        return super().update()

    def draw(self, surface):
        surface.blit(self.image, (0, 0))
