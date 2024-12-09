import minimal_pygame
import pygame


def pygame_wrapper(coro):
    yield from coro


def test_minimal_pygame():
    wrap = pygame_wrapper(minimal_pygame.minimal_pygame(testing=True))
    wrap.send(None)  # prime the coroutine
    # Create a dictionary of attributes for the future TESTEVENT
    attr_dict = {"instruction": "draw_rectangle"}
    response = wrap.send(attr_dict)
    assert response == pygame.Color("white")
