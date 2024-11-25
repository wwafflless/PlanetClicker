import pygame

pygame.init()

from src.scene.manager import SceneManager
from src.scene.title import TitleScene


def run_game(width, height, fps):
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    scene_manager = SceneManager()
    initial_scene = TitleScene(manager=scene_manager)
    scene_manager.push_scene(initial_scene)

    while scene_manager.stack:
        delta = clock.tick(60) / 1000
        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            if quit_attempt:
                if scene_manager.is_empty():
                    pygame.quit()
                    return
                else:
                    scene_manager.pop_scene()
            else:
                filtered_events.append(event)

        scene_manager.handle_input(filtered_events, pressed_keys)
        scene_manager.update()
        scene_manager.render(screen)

        # active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)
