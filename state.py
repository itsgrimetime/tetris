import pygame
import glass
from pygame.locals import *

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
	self.font = pygame.font.Font(None, 36)
	self.glass = glass.Glass(self.game, self)
	self.fall_delta = self.move_delta = 0.0
	self.points = 0

    def update(self, delta):
	no_blocks = not len(self.glass.blocks)
	if no_blocks or not self.glass.blocks[-1].moving:
	    self.glass.add_random_block()
	else:
	    if self.fall_delta > 200.0:
		self.fall_delta = 0.0
		self.glass.update(delta)
	    else:
		self.fall_delta += delta

	    if self.move_delta > 50.0:
		pygame.event.pump()
		keystate = pygame.key.get_pressed()
		if len(self.glass.blocks) > 0:
		    if keystate[K_LEFT]:
			self.glass.blocks[-1].move_left()
		    elif keystate[K_RIGHT]:
			self.glass.blocks[-1].move_right()
		    elif keystate[K_UP]:
			self.glass.blocks[-1].rotate_cw()
		    elif keystate[K_DOWN]:
			self.glass.blocks[-1].rotate_ccw()
		if keystate[K_SPACE]:
		    self.glass.update(delta)
		    self.fall_delta = 0.0
		self.move_delta = 0.0
	    else:
		self.move_delta += delta

    def draw(self, delta):
	self.game.screen.blit(self.background, (0, 0))
	black = (0, 0, 0)
	points = self.font.render("{points}".format \
		(points=self.points), True, black)
	self.game.screen.blit(points, (320, 430))
	self.glass.draw(delta)
