from tomlkit import TOMLDocument
import os
from dataclasses import dataclass
from types import SimpleNamespace
from planetclicker.data.parser import Parser

import pygame


def _load_font(font_name, size) -> pygame.font.Font:
    path = os.path.join("asset", "font", "free", font_name)
    return pygame.font.Font("asset/font/free/" + font_name, size)


class FontsParser(Parser[TOMLDocument]):
    def parse(self, data: TOMLDocument) -> dict:
        fonts = dict()
        for key, val in data.items():
            print(key)
            if key == "font":
                for k, v in val.items():
                    font_key: str = k
                    font_path = os.path.join("asset", "font", "free", v["name"])
                    font_size: int = v["size"]
                    font = pygame.font.Font(
                        font_path,
                        font_size,
                    )
                    fonts.update({font_key: font})
        return fonts
