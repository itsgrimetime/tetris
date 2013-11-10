import pygame, copy

class Block():

    BLOCKS = {
	    "I" :  [["E", "E", "E", "E"],
		    ["I", "I", "I", "I"],
		    ["E", "E", "E", "E"],
		    ["E", "E", "E", "E"]],

	    "O"	:  [["O", "O"],
		    ["O", "O"]],

	    "T"	:  [["E", "T", "E"],
		    ["T", "T", "T"],
		    ["E", "E", "E"]],

	    "S"	:  [["E", "S", "S"],
		    ["S", "S", "E"],
		    ["E", "E", "E"]],

	    "Z"	:  [["Z", "Z", "E"],
		    ["E", "Z", "Z"],
		    ["E", "E", "E"]],

	    "J" :  [["J", "E", "E"],
		    ["J", "J", "J"],
		    ["E", "E", "E"]],

	    "L"	:  [["E", "E", "L"],
		    ["L", "L", "L"],
		    ["E", "E", "E"]],
	    }

    colors = [("I", "cyan"), ("O", "yellow"), ("T", "purple"), ("S", "green"), \
	    ("Z", "red"), ("J", "blue"), ("L", "orange")]

    IMAGES = {}
    for block, color in colors:
	IMAGES[block] = pygame.image.load('images/' + color + 'block.png')

    def __init__(self, shape, glass):
	self.x = 3
	self.y = 0
	self.rot = 0
	self.shape = shape
	self.arr = copy.copy(Block.BLOCKS[shape])
	self.moving = True
	self.glass = glass
	self.image = Block.IMAGES[shape]

    def move(self):
	new_block = copy.copy(self)
	new_block.y += 1
	if self.moving and self.glass.is_valid_move(new_block):
	    self.y += 1
	    return True
	else:
	    return False

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
	new_block = copy.copy(self)
	new_block.arr = zip(*self.arr[::-1])
	if self.glass.is_valid_move(new_block):
	    self.arr = zip(*self.arr[::-1])

    def rotate_ccw(self):
	new_block = copy.copy(self)
	new_block.arr = zip(*self.arr)[::-1]
	if self.glass.is_valid_move(new_block):
	    self.arr = zip(*self.arr)[::-1]



