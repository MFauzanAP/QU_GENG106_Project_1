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
	global screen, pen
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
	RATIO = shape.input_props['height']['value'] / shape.input_props['width']['value']

	# Calculate rectangle width and height based on ratio
	WIDTH = 500 if RATIO <= 1 else (1 / RATIO) * 500
	HEIGHT = 500 if RATIO >= 1 else RATIO * 500

	# Setup fill
	pen.fillcolor('black')
	pen.begin_fill()
 
	# Start from top left
	pen.goto(-WIDTH / 2, HEIGHT / 2)
 
	# Repeat 4 times to draw each side
	for i in range(4):
         
		# Draw width or height depending on which side is selected
		pen.forward(WIDTH if i % 2 == 0 else HEIGHT)
  
		# Rotate 90 degrees
		pen.right(90)
  
	# Stop fill
	pen.end_fill()
 
	# Write dimensions

	# Stop turtle from closing
	input('')