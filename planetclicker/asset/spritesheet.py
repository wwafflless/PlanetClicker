import pygame


from pygame.sprite import Sprite


class SpriteSheet:

    def __init__(self, filename):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

    def image_at(self, rectangle, colorkey=None):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey=None):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey=None):
        """Load a whole strip of images, and return them as a list."""
        tups = [
            (rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
            for x in range(image_count)
        ]
        return self.images_at(tups, colorkey)


class AnimatedSprite(Sprite):
    """A sprite with an animation."""

    def __init__(self, filename: str) -> None:
        super().__init__()
        self.sheet = SpriteSheet(filename)
        self._index = 0
        self.size = 51
        image_0 = self.sheet.image_at((0, 0, 51, 51))
        rect = image_0.get_rect()
        self._images = self.sheet.load_strip(rect, 10, (0, 0, 51, 51))

    @property
    def current_rect(self):
        self.rect = self.current_image.get_rect()
        self.rect.topleft = (0, 0)
        return self.rect

    @property
    def current_image(self):
        return self._images[self._index]

    def update(self) -> None:
        """Update the animation frame."""
        self._index = (self._index + 1) % len(self._images)

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the sprite to the screen."""
        screen.blit(self.current_image, self.current_rect)
