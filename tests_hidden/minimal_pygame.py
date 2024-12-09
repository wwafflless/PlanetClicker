import pygame


TESTEVENT = pygame.event.custom_type()


def minimal_pygame(testing: bool = False):
    pygame.init()
    game_window_sf = pygame.display.set_mode(
        size=(400, 300),
    )
    pygame.display.flip()
    game_running = True
    while game_running:
        # Hook for testing
        if testing:
            attr_dict = yield
            test_event = pygame.event.Event(TESTEVENT, attr_dict)
            pygame.event.post(test_event)
        # Main game loop:
        pygame.time.wait(1000)
        for event in pygame.event.get():
            # React to closing the pygame window:
            if event.type == pygame.QUIT:
                game_running = False
                break
            # React to keypresses:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    # distinguish between Q and Ctrl-Q
                    mods = pygame.key.get_mods()
                    # End main loop if Ctrl-Q was pressed
                    if mods & pygame.KMOD_CTRL:
                        game_running = False
                        break
            # React to TESTEVENTS:
            if event.type == TESTEVENT:
                if event.instruction == "draw_rectangle":
                    filled_rect = game_window_sf.fill(
                        pygame.Color("white"), pygame.Rect(50, 50, 50, 50)
                    )
                    pygame.display.update([filled_rect])
                    pygame.time.wait(1000)
                    if testing:
                        # Yield the color value of the pixel at (50, 50) back to pytest
                        yield game_window_sf.get_at((50, 50))
    pygame.quit()


if __name__ == "__main__":
    minimal_pygame()
