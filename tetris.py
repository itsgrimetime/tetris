#/user/bin/env python

import os, pygame
from pygame.locals import *

class GameEngine():

    def __init__(self, screen):
	self.screen = screen
	self.states = []
	self.is_running = True

    def change_state(self, state):
	self.states.append(state)

    def update(self, delta):
	if len(self.states) > 0:
	    self.states[-1].update(delta)

    def draw(self, delta):
	if len(self.states) > 0:
	    self.states[-1].draw(delta)
	    pygame.display.flip()

class MainMenuState():

    def __init__(self, game):
	self.game = game
	self.background = pygame.image.load('images/menu.png')

    def update(self, delta):
	for event in pygame.event.get():
	    if event.type == MOUSEBUTTONDOWN:
		x, y = pygame.mouse.get_pos()
		if x > 80 and y > 308 and x < 513 and y < 475:
		    self.game.change_state(TetrisGameState(self.game))

    def draw(self, delta):
	self.game.screen.blit(self.background, (0, 0))

class TetrisGameState():

    def __init__(self, game):
	self.game = game;
	self.background = pygame.image.load('images/background.png')
	# self.font = pygame.font.Font(None, 36)
	# self.glass = Glass()
	self.fall_delta = self.move_delta = 0.0

    def update(self, delta):
	if self.fall_delta > 100.0:
	    self.fall_delta = 0.0
	    # glass.update
	else:
	    self.fall_delta += delta

    def draw(self, delta):
	self.game.screen.blit(self.background, (0, 0))

def main():

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Tetris, Bitch!')
    pygame.mouse.set_visible(1)

    # TODO move this to a specific gamestate class

    clock = pygame.time.Clock()
    game = GameEngine(screen)
    menu = MainMenuState(game)
    game.change_state(menu)

    while game.is_running:
	delta = clock.tick(60)
	game.draw(delta)
	game.update(delta)

main()
