import pygame, random
import block

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
	self.frozen_block_image = pygame.image.load('images/frozen_block.png')

    def update(self, delta):
	for block in self.blocks:
	    block.move()

    def draw(self, delta):
	for i in range(len(self.glass)):
	    for j in range(len(self.glass[i]))[2:len(self.glass[i])]:
		x = 180 + 16 * i
		y = 16 + 16 * j
		if self.glass[i][j] == 0:
		    self.game.screen.blit(self.block_image, (x, y))
		else:
		    self.game.screen.blit(self.frozen_block_image, (x, y))
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
	keys = block.Block.BLOCKS.keys()
	type = keys[random.randint(0, 6)]
	self.add_block(block.Block(block.Block.BLOCKS[type], self))

    def is_valid_move(self, block):
	# check to make sure block is not outside
	# left / right boundaries

	if block.x < 0:
	    return False
	elif block.x + len(block.arr[0]) > 10:
	    return False
	elif block.y + len(block.arr) > 22:
	    return False
	# also check to make sure block isnt on top of another
	# block that is currently set in the glass.
	for i, row in enumerate(block.arr):
	    # print row
	    # print i
	    for j in range(len(row)):
		if block.x + j <= 10 and block.y + i < 22:
		    print "%d, %d : %d" % (block.x + j, block.y + i, \
			    self.glass[block.x + j][block.y + i])

		    if self.glass[block.x + j][block.y + i] != 0 and \
			    block.arr[i][j] != 0:
			print "we hit another block, yo"
			return False
	print "\n"
	return True

    def freeze_block(self, block):
	for i, row in enumerate(block.arr):
	    for j in range(len(row)):
		if block.arr[i][j] == 1:
		    self.glass[block.x + j][block.y + i] = \
			block.arr[i][j]

