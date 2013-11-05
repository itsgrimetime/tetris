import pygame

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
