# Imports
import turtle

# Declare constants
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750
DIMENSIONS_OFFSET = 25
SIZE_LIMIT = 100
PEN_SIZE = 2
PEN_SPEED = 50
BACKGROUND_COLOR = (199, 233, 248)
PEN_COLOR = (50, 50, 50)

# Function used to set up turtle object
def setup_turtle():

	# Initialise a new turtle object as well as screen
	global screen, pen
	screen = turtle.getscreen()
	pen = turtle.Turtle()

	# Set up screen
	screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
	screen.colormode(255)
	screen.bgcolor(BACKGROUND_COLOR)

	# Setup pen
	pen.color(PEN_COLOR)
	pen.pensize(PEN_SIZE)
	pen.speed(PEN_SPEED)
	pen.penup()
	pen.hideturtle()

# Function used to draw rectangle with the correct dimensions
def draw_rectangle(shape):

	# Calculate ratio of height to width
	ratio = shape.input_props['height']['value'] / shape.input_props['width']['value']

	# Clamp ratio to avoid very tiny rectangles
	ratio = min(SIZE_LIMIT, max(1 / SIZE_LIMIT, ratio))

	# Calculate rectangle width and height based on ratio
	WIDTH = 500 if ratio <= 1 else (1 / ratio) * 500
	HEIGHT = 500 if ratio >= 1 else ratio * 500

	# Setup fill
	pen.fillcolor(PEN_COLOR)
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

	# Write title
	pen.goto(0, (HEIGHT / 2) + DIMENSIONS_OFFSET)
	pen.write('Rectangle', align = 'center', font = ('Arial', 16, 'bold'))

	# Write dimensions
	pen.goto(0, (-HEIGHT / 2) - DIMENSIONS_OFFSET)
	pen.write(f'{shape.input_props["width"]["value"]} {shape.input_props["width"]["unit"]}', align = 'center')
	pen.goto((-WIDTH / 2) - (DIMENSIONS_OFFSET / 2), 0)
	pen.write(f'{shape.input_props["height"]["value"]} {shape.input_props["height"]["unit"]}', align = 'right')

	# Stop turtle from closing
	input('')