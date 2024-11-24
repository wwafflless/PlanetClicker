import pygame

pygame.init()


def run_game(width, height, fps, starting_scene):
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
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
                active_scene.kill()
            else:
                filtered_events.append(event)

        active_scene.handle_input(filtered_events, pressed_keys)
        active_scene.update()
        active_scene.render(screen)

        active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)


# class Game:
#     def __init__(self, width=800, height=600):
#         self.screen = pygame.display.set_mode((width, height))
#         self.clock = pygame.time.Clock()
#         self.running = True
#         self.size = pygame.Rect(0, 0, width, height)
#         self.mana = 0
#         self.scene = ClickerScene()

#     def run(self):
#         while self.running:
#             self.handle_input()
#             self.update()
#             self.draw()
#             self.clock.tick(60)
#         pygame.quit()
#         sys.exit()

#     def handle_input(self):
#         self.scene.handle_input(pygame.event.get())

#     def update(self):
#         self.scene.update()

#     def draw(self):
#         self.scene.draw(self.screen)
#         pygame.display.flip()
