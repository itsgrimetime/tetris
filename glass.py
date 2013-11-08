import pygame, random
import block

class Glass():

    def __init__(self, game):
	self.game = game
	self.glass = []
	for i in range(10):
	    self.glass.append([])
	    for j in range(22):
		self.glass[i].append('E')
	self.blocks = []
	self.block_image = pygame.image.load('images/block.png')
	self.frozen_block_image = pygame.image.load('images/frozen_block.png')

    def update(self, delta):
	for block in self.blocks:
	    block.move()

    def draw(self, delta):
	for i in range(len(self.glass)):
	    for j in range(len(self.glass[i]))[2:len(self.glass[i])]:
		x = 180 + 16 * i
		y = 16 + 16 * j
		if self.glass[i][j] == "E":
		    self.game.screen.blit(self.block_image, (x, y))
		else:
		    self.game.screen.blit(self.frozen_block_image, (x, y))
	self.draw_blocks(delta)

    def draw_blocks(self, delta):
	for block in self.blocks:
	    for i in range(len(block.arr)):
		for j in range(len(block.arr[i])):
		    if block.arr[i][j] != 'E' and (block.y + i) > 1:
			drawx = 180 + 16 * block.x + 16 * j
			drawy = 16 + 16 * block.y + 16 * i
			self.game.screen.blit(block.image, (drawx, drawy))

    def add_block(self, block):
	print "adding block"
	print "arr: {arr}".format(arr=block.arr)
	self.blocks.append(block)

    def add_random_block(self):
	keys = block.Block.BLOCKS.keys()
	type = keys[random.randint(0, 6)]
	self.add_block(block.Block(type, self))

    def is_valid_move(self, block):
	for i, row in enumerate(block.arr):
	    for j in range(len(row)):
		is_block_in_tet = block.arr[i][j] != 'E'
		if is_block_in_tet:
		    is_out_of_glass_x = block.x + j > 9 or block.x + j < 0
		    is_out_of_glass_y = block.y + i > 21 or block.y + i < 0
		    is_out_of_glass = is_out_of_glass_x or is_out_of_glass_y
		    if is_out_of_glass:
			print "block out of glass"
			return False
		    else:
			print self.glass[block.x + j][block.y + i]
			if self.glass[block.x + j][block.y + i] != 'E':
			    print "block on other block"
			    return False
	print "all good"
	return True

    def freeze_block(self, block):
	for i, row in enumerate(block.arr):
	    for j in range(len(row)):
		if block.arr[i][j] != 'E':
		    self.glass[block.x + j][block.y + i] = \
			block.arr[i][j]

