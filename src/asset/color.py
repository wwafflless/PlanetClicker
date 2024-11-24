from types import SimpleNamespace

# Space Time (https://www.schemecolor.com/space-time.php)
# Middle Yellow Red (#E6BF73)
# Teal Blue (#2B7F94)
# Deep Koamaru (#2E3870)
# Space Cadet (#221F59)
# Midnight (#67166E)
# Maximum Purple (#823982).


import pygame


class Color(SimpleNamespace):
    # text = (254, 254, 254)
    # background = (1, 1, 1)
    # brand = (200, 210, 255)
    # accent = (240, 210, 10)
    text = pygame.Color("#eeeeeeee")
    background = pygame.Color("#221f59")
    brand = pygame.Color("#e6bf73")
    accent = pygame.Color("#2b7f94")
