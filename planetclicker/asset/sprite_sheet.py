import pygame
from pygame.sprite import Sprite


class SpriteSheet(Sprite):
    def __init__(self, filename):
        """Loads SpriteSheet from a given file"""
        with open(filename) as f:
            self.sheet = pygame.image.load(f).convert()
            print(dict(sheet=self.sheet))
        # except pygame.error:
        #     print("Unable to load spritesheet image:", filename)
        #     raise Exception("Unable to load SpriteSheet image")

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey=None):
        """Loads image from x,y,x+offset,y+offset"""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey=None):
        """Loads multiple images, supply a list of coordinates"""
        return [self.image_at(rect, colorkey) for rect in rects]

    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey=None):
        "Loads a strip of images and returns them as a list"
        tups = [
            (rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
            for x in range(image_count)
        ]
        return self.images_at(tups, colorkey)


class SpriteStripAnim(Sprite):
    """
    Sprite strip animator

    Params:
    - filename : str
    - rect : tuple
    - count : int
    - colorkey : int or None
    - loop : bool
    - frames : int
    """

    def __init__(self, filename, rect, count, colorkey=None, loop=True, frames=1):
        """
        loop is a boolean that, when True, causes the next() method to
        loop. If False, the terminal case raises StopIteration.

        frames is the number of ticks to return the same image before
        the iterator advances to the next image.
        """
        super().__init__()
        ss = SpriteSheet(filename)
        self.images = ss.load_strip(rect, count, colorkey)
        self.image = self.images[0]
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames

    def iter(self):
        self.i = 0
        self.f = self.frames
        return self

    def next(self):
        if self.i >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image

    def update(self):
        self.image = self.next()

    def __add__(self, ss):
        self.images.extend(ss.images)
        return self
