import pygame, copy

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

    def __init__(self, arr, glass):
	self.x = 3
	self.y = 0
	self.rot = 0
	self.arr = arr
	self.moving = True
	self.glass = glass
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
	new_block = copy.copy(self)
	new_block.y += 1
	if self.moving and self.glass.is_valid_move(new_block):
	    self.y += 1
	else:
	    self.moving = False
	    self.glass.freeze_block(self)

    def move_left(self):
	new_block = copy.copy(self)
	new_block.x -= 1
	if self.glass.is_valid_move(new_block):
	    self.x -= 1

    def move_right(self):
	new_block = copy.copy(self)
	new_block.x += 1
	if self.glass.is_valid_move(new_block):
	    self.x += 1

    def rotate_cw(self):
	self.arr = zip(*self.arr[::-1])

    def rotate_ccw(self):
	self.arr = zip(*self.arr)[::-1]

