from dataclasses import dataclass

import pygame
import tomlkit


@dataclass
class TOMLReader:
    path: str
    # def read(self, filename: str):
    #     s

    def get(self, key: str):
        return self.data.get(key)

    def gets(self, *keys: str):
        cfg = self.data
        for key in keys:
            cfg = cfg.get(key)
        return cfg

    @property
    def data(self):
        with open(self.path) as fp:
            doc = tomlkit.load(fp)
            # doc.add("path", string(self.path))
            return doc


@dataclass
class FontReader(TOMLReader):
    path: str

    @property
    def fonts(self):
        fonts = {}
        for label, props in self.data.items():
            path = os.path.join("asset", "font", "free", props["name"])
            fonts[label] = pygame.font.Font(path, props["size"])
        return fonts
