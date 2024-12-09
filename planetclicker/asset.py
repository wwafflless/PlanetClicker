import os
from dataclasses import dataclass


@dataclass
class Asset:
    name: str
    kind: str
    ext: str

    @classmethod
    def Font(cls, name):
        return Asset(name, "font", "ttf")

    @classmethod
    def Image(cls, name):
        return Asset(name, "image", "png")

    def path(self):
        return os.path.join("assets", self.kind, f"{self.name}.{self.ext}")


Fonts = dict(
    jersey25=Asset.Font("Jersey25-Regular"),
    pixelated_elegance=Asset.Font("PixelatedElegance"),
    pixelify_sans=Asset.Font("PixelifySans-Regular"),
    roboto=Asset.Font("RobotoMono-Regular"),
    space_quest=Asset.Font("SpaceQuest"),
    thaleah_fat=Asset.Font("ThaleahFat"),
)

Images = dict(earth=Asset.Image("earth"))
