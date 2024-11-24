import pygame
from src.asset.color import Color
from src.asset.font import text_font, title_font
from src.particle.bg_star import BGStarSystem
from src.scene import Scene
from src.scene.main import MainScene


class TitleScene(Scene):
    def __init__(self):
        super().__init__("title")
        self.title_text = title_font.render(
            "Planet Clicker",
            False,
            Color.brand,
        )
        self.instruction_text = text_font.render(
            "Press ENTER to start",
            False,
            Color.accent,
        )
        self.particles = BGStarSystem(n=100)

    def handle_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.switch(MainScene())

    def update(self):
        self.particles.update()

    def render(self, screen):
        screen.fill(Color.background)
        self.particles.draw(screen)
        screen.blit(
            self.title_text,
            (
                400 - self.title_text.get_width() // 2,
                200,
            ),
        )
        screen.blit(
            self.instruction_text,
            (
                400 - self.instruction_text.get_width() // 2,
                400,
            ),
        )
