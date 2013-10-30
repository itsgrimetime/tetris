require 'rubygems'
require 'gosu'

class GameWindow < Gosu::Window

    def initialize
	super 640, 480, false
	self.caption = "Tetris Test"
	@background_image = Gosu::Image.new(self, "images/background.png")
	@font = Gosu::Font.new(self, Gosu::default_font_name, 20)
	@player = Player.new(self)
	@glass = Glass.new(self)
	@fall_delta = 0.0
	@move_delta = 0.0
    end

    def update
	if @move_delta > 100.0
	    if button_down? Gosu::KbLeft or button_down? Gosu::GpLeft then
		@player.move_left
	    end
	    if button_down? Gosu::KbRight or button_down? Gosu::GpRight then
		@player.move_right
	    end
	    if button_down? Gosu::KbUp or button_down? Gosu::GpButton0 then
		@player.rotate_counter_clockwise
	    end
	    if button_down? Gosu::KbDown or button_down? Gosu::GpButton1 then
		@player.rotate_clockwise
	    end
	    if button_down? Gosu::KbSpace then
		@player.fall_faster
	    end
	    @move_delta = 0.0
	else
	    @move_delta += self.update_interval
	end
	if @fall_delta > 1000.0
	    @player.move
	    @fall_delta = 0.0
	else
	    @fall_delta += self.update_interval
	end
    end

    def draw
	@background_image.draw(0, 0, 0)
	@glass.draw
	@player.draw
	@font.draw("Player Coords (#{@player.x}, #{@player.y})", 10, 10, 0)
    end
end

class Block

    I = [[0, 0, 0, 0],
	[1, 1, 1, 1],
	[0, 0, 0, 0],
	[0, 0, 0, 0]]

    O = [[1, 1],
	[1, 1]]

    T	= [[0, 1, 0],
	[1, 1, 1]]

    S	= [[0, 1, 1],
	[1, 1, 0]]

    Z	= [[1, 1, 0],
	[0, 0, 1]]

    J   = [[1, 0, 0],
	[1, 1, 1]]

    L	= [[0, 0, 1],
	[1, 1, 1]]

    BLOCKS = [I, O, T, S, Z, J, L]

end

class Glass

    BLOCK_TYPES = ["green", "red", "cyan", "purple", "yellow", "orange", "blue", "empty"]

    def initialize(window)
	@window = window
	@glass = Array.new(10, Array.new(22, 'E'))
	@block_images = load_block_images
    end

    def draw
	for i in 0..@glass.length - 1
	    for j in 2..@glass[i].length - 1
		case @glass[i][j]
		when nil
		    image = @block_images["empty"]
		when 'g'
		    image = @block_images["green"]
		when 'r'
		    image = @block_images["red"]
		when 'c'
		    image = @block_images["cyan"]
		when 'p'
		    image = @block_images["purple"]
		when 'y'
		    image = @block_images["yellow"]
		when 'o'
		    image = @block_images["orange"]
		when 'b'
		    image = @block_images["blue"]
		else
		    image = @block_images["empty"]
		end
		image.draw(160 + 16 * i, 16 + 16 * j, 0)
	    end
	end
    end

    def clear_rows
    end

    def load_block_images
	@block_images = Hash.new
	BLOCK_TYPES.each do |type|
	    @block_images[type] = Gosu::Image.new(@window, "images/#{type}block.png")
	end
	@block_images
    end

end

class Tetromino

    def initialize(window)
    end

end

class Player

    def initialize(window)
	@x = 160
	@y = 16
	@rot = 0
	@fall_speed = 1
	@score = 0
	@tetromino = nil
	@image = Gosu::Image.new(window, "images/orangeblock.png")
    end

    def move
	@y += 16 * @fall_speed
    end

    def rotate_clockwise
	@rot += 90
    end

    def rotate_counter_clockwise
	@rot -= 90
    end

    def draw
	@image.draw(@x, @y, 0)
    end

    def move_left
	@x -= 16
    end

    def move_right
	@x += 16
    end

    def rotate_counter_clockwise
    end

    def rotate_clockwise
    end

    def fall_faster
	@fall_speed += 1
    end

    def x
	@x
    end

    def y
	@y
    end

end

window = GameWindow.new
window.show
