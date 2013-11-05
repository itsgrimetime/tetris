#/user/bin/env python

import engine, block, glass, state
import os, pygame, copy

def enum(**enums):
    return type('Enum', (), enums)



def main():

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Tetris, Bitch!')
    pygame.mouse.set_visible(1)

    # TODO move this to a specific gamestate class

    clock = pygame.time.Clock()
    game = engine.GameEngine(screen)
    menu = state.MainMenuState(game)
    game.change_state(menu)

    while game.is_running:
	delta = clock.tick(60)
	game.draw(delta)
	game.update(delta)

main()
