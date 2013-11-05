#/user/bin/env python

import os, pygame, random
from pygame.locals import *

def enum(**enums):
    return type('Enum', (), enums)

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
	self.glass = Glass(self.game)
	self.fall_delta = self.move_delta = 0.0

    def update(self, delta):
	no_blocks = not len(self.glass.blocks)
	if no_blocks or not self.glass.blocks[-1].moving:
	    self.glass.add_random_block()
	else:
	    if self.fall_delta > 600.0:
		self.fall_delta = 0.0
		self.glass.update(delta)
	    else:
		self.fall_delta += delta

	    if self.move_delta > 100.0:
		pygame.event.pump()
		keystate = pygame.key.get_pressed()

		if keystate[K_LEFT]:
		    self.glass.blocks[-1].move_left()
		elif keystate[K_RIGHT]:
		    self.glass.blocks[-1].move_right()
		elif keystate[K_DOWN]:
		    self.glass.update(delta)
		    self.fall_delta = 0.0
		self.move_delta = 0.0
	    else:
		self.move_delta += delta

    def draw(self, delta):
	self.game.screen.blit(self.background, (0, 0))
	self.glass.draw(delta)

class Glass():

    def __init__(self, game):
	self.game = game
	self.glass = []
	for i in range(10):
	    self.glass.append([])
	    for j in range(22):
		self.glass[i].append(0)
	self.blocks = []
	self.block_image = pygame.image.load('images/block.png')

    def update(self, delta):
	for block in self.blocks:
	    block.move()

    def draw(self, delta):
	for i in range(len(self.glass)):
	    for j in range(len(self.glass[i]))[2:len(self.glass[i])]:
		self.game.screen.blit(self.block_image, (180 + 16 * i, \
			16 + 16 * j))
	self.draw_blocks(delta)

    def draw_blocks(self, delta):
	for block in self.blocks:
	    for i in range(len(block.arr)):
		for j in range(len(block.arr[i])):
		    if block.arr[i][j] == 1 and (block.y + i) > 1:
			drawx = 180 + 16 * block.x + 16 * j
			drawy = 16 + 16 * block.y + 16 * i
			self.game.screen.blit(block.image, (drawx, drawy))

    def add_block(self, block):
	self.blocks.append(block)

    def add_random_block(self):
	print "adding random block"
	keys = Block.BLOCKS.keys()
	type = keys[random.randint(0, 6)]
	self.add_block(Block(Block.BLOCKS[type]))


class Block():

    BLOCKS = {
	    "I" : [[0, 0, 0, 0],
		[1, 1, 1, 1],
		[0, 0, 0, 0],
		[0, 0, 0, 0]],

	    "O"	: [[1, 1],
		[1, 1]],

	    "T"	: [[0, 1, 0],
		[1, 1, 1]],

	    "S"	: [[0, 1, 1],
		[1, 1, 0]],

	    "Z"	: [[1, 1, 0],
		[0, 1, 1]],

	    "J"   : [[1, 0, 0],
		[1, 1, 1]],

	    "L"	: [[0, 0, 1],
		[1, 1, 1]],
	    }

    def __init__(self, arr):
	self.x = 3
	self.y = 0
	self.rot = 0
	self.arr = arr
	self.moving = True
	if arr == Block.BLOCKS["I"]:
	    self.image = pygame.image.load('images/cyanblock.png')
	    self.color = (0, 255, 255)
	elif arr == Block.BLOCKS["O"]:
	    self.image = pygame.image.load('images/yellowblock.png')
	    self.color = (255, 255, 0)
	elif arr == Block.BLOCKS["T"]:
	    self.image = pygame.image.load('images/purpleblock.png')
	    self.color = (255, 0, 255)
	elif arr == Block.BLOCKS["S"]:
	    self.image = pygame.image.load('images/greenblock.png')
	    self.color = (0, 255, 0)
	elif arr == Block.BLOCKS["Z"]:
	    self.image = pygame.image.load('images/redblock.png')
	    self.color = (255, 0, 0)
	elif arr == Block.BLOCKS["J"]:
	    self.image = pygame.image.load('images/blueblock.png')
	    self.color = (0, 0, 255)
	elif arr == Block.BLOCKS["L"]:
	    self.image = pygame.image.load('images/orangeblock.png')
	    self.color = (255, 128, 0)

    def move(self):
	print "moving block"
	if self.moving:
	    if self.y < 20:
		self.y += 1
	    else:
		self.moving = False
		# dim color of block

    def move_left(self):
	# if self.glass.is_valid_move(self.x - 1):
	self.x -= 1

    def move_right(self):
	# if self.glass.is_valid_move(self.x + 1):
	self.x += 1

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
