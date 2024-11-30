import pygame

from planetclicker.sprite.sprite_sheet import SpriteSheet


class AnimatedSprite(pygame.sprite.Sprite):
    """A sprite with an animation."""

    @classmethod
    def from_data(cls, data: dict): ...

    def __init__(
        self,
        name: str,
        w: int,
        h: int,
        frames: int,
    ) -> None:
        super().__init__()
        self.w = w
        self.h = h
        self.size = min([w, h])
        self.sheet = SpriteSheet(
            name=name,
            ext="png",
            w=self.size,
            h=self.size,
        )
        self._index = 0
        rect = pygame.Rect(0, 0, self.w, self.h)
        self._images = self.sheet.load_strip(rect, frames)

    @property
    def current_image(self):
        return self._images[self._index]

    def update(self) -> None:
        """Update the animation frame."""
        self._index = (self._index + 1) % len(self._images)

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the sprite to the screen."""
        rect = self.current_image.get_rect()
        rect.topleft = 0, 0
        screen.blit(self.current_image, rect)
