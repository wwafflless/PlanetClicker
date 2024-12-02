from dataclasses import dataclass

import pygame
import tomlkit
from src.data.loader import FontLoader, ImageLoader, TextLoader, TomlLoader


def test_toml_loader():
    toml_file = TomlLoader("files/test.toml")
    assert toml_file.data.get("desc") == "test"


def test_text_loader():
    text_file = TextLoader("files/test.txt")
    print(text_file.content)


# def test_font_loader():
#     font_loader = FontLoader("example.ttf", 24)
#     print(font_loader.font)


def test_image_loader():
    image_loader = ImageLoader("files/test.png", 20)
    image_loader.image.show()  # display the image


# @dataclass
# class TOMLReader:
#     path: str

#     def get(self, key: str):
#         return self.data.get(key)

#     def gets(self, *keys: str):
#         cfg = self.data
#         for key in keys:
#             cfg = cfg.get(key)
#         return cfg

#     @property
#     def data(self):
#         with open(self.path) as fp:
#             doc = tomlkit.load(fp)
#             # doc.add("path", string(self.path))
#             return doc


# @dataclass
# class FontReader(TOMLReader):
#     path: str

#     @property
#     def fonts(self):
#         fonts = {}
#         for label, props in self.data.items():
#             path = os.path.join("asset", "font", "free", props["name"])
#             fonts[label] = pygame.font.Font(path, props["size"])
#         return fonts
