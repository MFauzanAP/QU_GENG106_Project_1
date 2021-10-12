# Imports
import turtle

# Declare constants
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750
PEN_SIZE = 2
PEN_SPEED = 50

# Function used to set up turtle object
def setup_turtle():

	# Initialise a new turtle object as well as screen
	screen = turtle.getscreen()
	pen = turtle.Turtle()

	# Set up screen
	screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
	screen.colormode(255)
	screen.bgcolor(199, 233, 248)

	# Setup pen
	pen.color('black')
	pen.pensize(PEN_SIZE)
	pen.speed(PEN_SPEED)
	pen.penup()

# Function used to draw rectangle with the correct dimensions
def draw_rectangle(shape):

	# Calculate ratio of height to width
	ratio = shape.input_props['height']['value'] / shape.input_props['width']['value']

	# Stop turtle from closing
	input('')