import pygame, random, copy
import block

class Glass():

    def __init__(self, game, state):
	self.state = state
	self.game = game
	self.glass = []
	for i in range(22):
	    self.glass.append([])
	    for j in range(10):
		self.glass[i].append('E')
	self.blocks = []
	self.next_block = None
	self.frozen_block_image = pygame.image.load('images/frozen_block.png')
	self.block_image = pygame.image.load('images/block.png')

    def update(self, delta):
	for block in self.blocks:
	    moved = block.move()
	    if not moved:
		self.moving = False
		self.freeze_block(block)
		self.blocks.remove(block)
	self.clear_full_rows()

    def draw(self, delta):
	for i, row in enumerate(self.glass[2:22]):
	    i = i + 2
	    for j, slot in enumerate(row):
		x = 180 + 16 * j
		y = 16 + 16 * i
		if self.glass[i][j] == "E":
		    self.game.screen.blit(self.block_image, (x, y))
		else:
		    self.game.screen.blit(self.frozen_block_image, (x, y))
	self.draw_blocks(delta)
	self.draw_ghost_block(delta)
	self.draw_next_block(delta)

    def draw_blocks(self, delta):
	for block in self.blocks:
	    for i in range(len(block.arr)):
		for j in range(len(block.arr[i])):
		    if block.arr[i][j] != 'E' and (block.y + i) > 1:
			drawx = 180 + 16 * block.x + 16 * j
			drawy = 16 + 16 * block.y + 16 * i
			self.game.screen.blit(block.image, (drawx, drawy))

    def draw_next_block(self, delta):
	if self.next_block != None:
	    for i, row in enumerate(self.next_block.arr):
		for j, piece in enumerate(row):
		    if piece != 'E':
			drawx = 25 + 16 * self.next_block.x + 16 * j
			drawy = 16 + 16 * self.next_block.y + 16 * i
			self.game.screen.blit(self.next_block.image, (drawx, drawy))

    def add_block(self, block):
	# print "adding block"
	# print "arr: {arr}".format(arr=block.arr)
	if self.next_block != None:
	    self.blocks.append(self.next_block)
	self.next_block = block

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
			# print "block out of glass"
			return False
		    else:
			if self.glass[block.y + i][block.x + j] != 'E':
			    # print "block on other block"
			    return False
	# print "all good"
	return True

    def clear_full_rows(self):
	total_score = 0
	for row in self.glass:
	    for elem in row:
		if elem == 'E':
		    break
	    else: # row with no empty spots
		self.glass.remove(row)
		new_row = ["E" for i in range(10)]
		self.glass.insert(0, new_row)
		total_score += 1
	if 2 ** total_score > 1:
	    self.state.points += 2 ** total_score

    def draw_ghost_block(self, delta):
	if len(self.blocks) > 0:
	    block = copy.copy(self.blocks[-1])
	    while (True):
		if not (block.move()):
		    break
	    block.image = block.IMAGES["X"]
	    for i, row in enumerate(block.arr):
		for j, elem in enumerate(row):
		    if elem != "E":
			drawx = 180 + 16 * block.x + 16 * j
			drawy = 16 + 16 * block.y + 16 * i
			self.game.screen.blit(block.image, (drawx, drawy))



    def freeze_block(self, block):
	for i, row in enumerate(block.arr):
	    for j in range(len(row)):
		if block.arr[i][j] != 'E':
		    self.glass[block.y + i][block.x + j] = \
			block.arr[i][j]

