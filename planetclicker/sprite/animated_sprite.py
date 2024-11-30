import pygame

from planetclicker.sprite.sprite_sheet import SpriteSheet


class AnimatedSprite(pygame.sprite.Sprite):
    """A sprite with an animation."""

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
        self.set_position(0, 0)
        rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self._images = self.sheet.load_strip(rect, frames)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    @property
    def current_image(self):
        return self._images[self._index]

    def update(self) -> None:
        """Update the animation frame."""
        self._index = (self._index + 1) % len(self._images)

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the sprite to the screen."""
        rect = self.current_image.get_rect()
        rect.topleft = self.x, self.y
        surface.blit(self.current_image, rect)
