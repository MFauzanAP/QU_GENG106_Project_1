# Imports
import turtle

# Declare constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
DIMENSIONS_OFFSET = 25
SHAPE_SIZE = 500
SIZE_LIMIT = 100
PEN_SIZE = 2
PEN_SPEED = 'fastest'
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
	WIDTH = SHAPE_SIZE if ratio <= 1 else (1 / ratio) * SHAPE_SIZE
	HEIGHT = SHAPE_SIZE if ratio >= 1 else ratio * SHAPE_SIZE

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
	pen.hideturtle()

	# Write title
	pen.goto(0, (HEIGHT / 2) + DIMENSIONS_OFFSET)
	pen.write('Rectangle', align = 'center', font = ('Arial', 16, 'bold'))

	# Write dimensions
	pen.goto(0, (-HEIGHT / 2) - DIMENSIONS_OFFSET)
	pen.write(f'{shape.input_props["width"]["value"]} {shape.input_props["width"]["unit"]}', align = 'center')
	pen.goto((-WIDTH / 2) - (DIMENSIONS_OFFSET / 2), 0)
	pen.write(f'{shape.input_props["height"]["value"]} {shape.input_props["height"]["unit"]}', align = 'right')

	# Stop turtle from closing
	input('Press any key to continue')

# Function used to draw circle with the correct dimensions
def draw_circle(shape):

	# Calculate diameter
	DIAMETER = SHAPE_SIZE

	# Setup fill
	pen.fillcolor(PEN_COLOR)
	pen.begin_fill()

	# Start from top left
	pen.goto(0, -DIAMETER / 2)
 
	# Draw circle
	pen.circle(DIAMETER / 2)

	# Stop fill
	pen.end_fill()
	pen.hideturtle()

	# Write title
	pen.goto(0, (DIAMETER / 2) + DIMENSIONS_OFFSET)
	pen.write('Circle', align = 'center', font = ('Arial', 16, 'bold'))

	# Write dimensions
	pen.goto(0, (-DIAMETER / 2) - DIMENSIONS_OFFSET)
	pen.write(f'{shape.input_props["diameter"]["value"]} {shape.input_props["diameter"]["unit"]}', align = 'center')

	# Stop turtle from closing
	input('Press any key to continue')

# Function used to draw donut with the correct dimensions
def draw_donut(shape):

	# Calculate diameters
	OUTER_DIAMETER = SHAPE_SIZE
	INNER_DIAMETER = (shape.input_props["inner_diameter"]["value"] / shape.input_props["outer_diameter"]["value"]) * SHAPE_SIZE

	# Setup fill
	pen.fillcolor(PEN_COLOR)
	pen.begin_fill()

	# Start from bottom middle
	pen.goto(0, -OUTER_DIAMETER / 2)

	# Draw outer circle
	pen.circle(OUTER_DIAMETER / 2)

	# Go to inner circle position
	pen.end_fill()
	pen.fillcolor(BACKGROUND_COLOR)
	pen.goto(0, -INNER_DIAMETER / 2)
	pen.begin_fill()

	# Draw inner hole
	pen.circle(INNER_DIAMETER / 2)

	# Stop fill
	pen.end_fill()
	pen.hideturtle()

	# Write title
	pen.goto(0, (OUTER_DIAMETER / 2) + DIMENSIONS_OFFSET)
	pen.write('Hollow Circular', align = 'center', font = ('Arial', 16, 'bold'))

	# Write dimensions
	pen.goto(0, 0)
	pen.write(f'{shape.input_props["inner_diameter"]["value"]} {shape.input_props["inner_diameter"]["unit"]}', align = 'center')
	pen.goto(0, (-OUTER_DIAMETER / 2) - DIMENSIONS_OFFSET)
	pen.write(f'{shape.input_props["outer_diameter"]["value"]} {shape.input_props["outer_diameter"]["unit"]}', align = 'center')

	# Stop turtle from closing
	input('Press any key to continue')

# Function used to draw t section with the correct dimensions
def draw_t_section(shape):

	# Extract data from input properties
	overall_width = shape.input_props['overall_width']['value']
	overall_height = shape.input_props['overall_height']['value']
	flange_width = shape.input_props['flange_width']['value']
	flange_height = shape.input_props['flange_height']['value']
	web_width = shape.input_props['web_width']['value']
	web_height = shape.input_props['web_height']['value']

	# Calculate ratio of height to width
	ratio = overall_height / overall_width

	# Clamp ratio to avoid very tiny shapes
	ratio = min(SIZE_LIMIT, max(1 / SIZE_LIMIT, ratio))

	# Calculate t section width and height based on ratio
	WIDTH = SHAPE_SIZE if ratio <= 1 else (1 / ratio) * SHAPE_SIZE
	HEIGHT = SHAPE_SIZE if ratio >= 1 else ratio * SHAPE_SIZE
	flange_width = (flange_width / overall_width) * WIDTH
	flange_height = (flange_height / overall_height) * HEIGHT
	web_width = (web_width / overall_width) * WIDTH
	web_height = (web_height / overall_height) * HEIGHT

	# Setup fill
	pen.fillcolor(PEN_COLOR)
	pen.begin_fill()

	# Start from top left
	pen.goto(-WIDTH / 2, HEIGHT / 2)

	# Repeat 4 times to draw each flange side
	for i in range(4):

		# Draw width or height depending on which side is selected
		pen.forward(flange_width if i % 2 == 0 else flange_height)

		# Rotate 90 degrees
		pen.right(90)

	# Go to web starting position
	pen.end_fill()
	pen.goto(-web_width / 2, (HEIGHT / 2) - flange_height)
	pen.begin_fill()

	# Repeat 4 times to draw each web side
	for i in range(4):

		# Draw width or height depending on which side is selected
		pen.forward(web_width if i % 2 == 0 else web_height)

		# Rotate 90 degrees
		pen.right(90)

	# Stop fill
	pen.end_fill()
	pen.hideturtle()

	# Write title
	pen.goto(0, (HEIGHT / 2) + (DIMENSIONS_OFFSET * 2))
	pen.write('T-Section', align = 'center', font = ('Arial', 16, 'bold'))
 
	# Write dimensions
	pen.goto(0, (HEIGHT / 2) + (DIMENSIONS_OFFSET / 2))
	pen.write(f'{shape.input_props["flange_width"]["value"]} {shape.input_props["flange_width"]["unit"]}', align = 'center')
	pen.goto((-WIDTH / 2) - (DIMENSIONS_OFFSET / 2), (HEIGHT / 2) - (flange_height / 2))
	pen.write(f'{shape.input_props["flange_height"]["value"]} {shape.input_props["flange_height"]["unit"]}', align = 'right')
	pen.goto(0, (-HEIGHT / 2) - DIMENSIONS_OFFSET)
	pen.write(f'{shape.input_props["web_width"]["value"]} {shape.input_props["web_width"]["unit"]}', align = 'center')
	pen.goto((-web_width / 2) - DIMENSIONS_OFFSET, (-flange_height / 2))
	pen.write(f'{shape.input_props["web_height"]["value"]} {shape.input_props["web_height"]["unit"]}', align = 'right')

	# Stop turtle from closing
	input('Press any key to continue')

# Function used to draw i section with the correct dimensions
def draw_i_section(shape):

	# Extract data from input properties
	overall_width = shape.input_props['overall_width']['value']
	overall_height = shape.input_props['overall_height']['value']
	flange_width = shape.input_props['flange_width']['value']
	flange_height = shape.input_props['flange_height']['value']
	web_width = shape.input_props['web_width']['value']
	web_height = shape.input_props['web_height']['value']

	# Calculate ratio of height to width
	ratio = overall_height / overall_width

	# Clamp ratio to avoid very tiny shapes
	ratio = min(SIZE_LIMIT, max(1 / SIZE_LIMIT, ratio))

	# Calculate t section width and height based on ratio
	WIDTH = SHAPE_SIZE if ratio <= 1 else (1 / ratio) * SHAPE_SIZE
	HEIGHT = SHAPE_SIZE if ratio >= 1 else ratio * SHAPE_SIZE
	flange_width = (flange_width / overall_width) * WIDTH
	flange_height = (flange_height / overall_height) * HEIGHT
	web_width = (web_width / overall_width) * WIDTH
	web_height = (web_height / overall_height) * HEIGHT

	# Setup fill
	pen.fillcolor(PEN_COLOR)
	pen.begin_fill()

	# Start from top left
	pen.goto(-WIDTH / 2, HEIGHT / 2)

	# Repeat 4 times to draw each flange side
	for i in range(4):

		# Draw width or height depending on which side is selected
		pen.forward(flange_width if i % 2 == 0 else flange_height)

		# Rotate 90 degrees
		pen.right(90)

	# Go to web starting position
	pen.end_fill()
	pen.goto(-web_width / 2, (HEIGHT / 2) - flange_height)
	pen.begin_fill()

	# Repeat 4 times to draw each web side
	for i in range(4):

		# Draw width or height depending on which side is selected
		pen.forward(web_width if i % 2 == 0 else web_height)

		# Rotate 90 degrees
		pen.right(90)

	# Start from top left
	pen.goto(-WIDTH / 2, -HEIGHT / 2)

	# Repeat 4 times to draw each flange side
	for i in range(4):

		# Draw width or height depending on which side is selected
		pen.forward(flange_width if i % 2 == 0 else flange_height)

		# Rotate 90 degrees
		pen.right(-90)

	# Stop fill
	pen.end_fill()
	pen.hideturtle()

	# Write title
	pen.goto(0, (HEIGHT / 2) + (DIMENSIONS_OFFSET * 2))
	pen.write('I-Section', align = 'center', font = ('Arial', 16, 'bold'))
 
	# Write dimensions
	pen.goto(0, (HEIGHT / 2) + (DIMENSIONS_OFFSET / 2))
	pen.write(f'{shape.input_props["flange_width"]["value"]} {shape.input_props["flange_width"]["unit"]}', align = 'center')
	pen.goto((-WIDTH / 2) - (DIMENSIONS_OFFSET / 2), (HEIGHT / 2) - (flange_height / 2))
	pen.write(f'{shape.input_props["flange_height"]["value"]} {shape.input_props["flange_height"]["unit"]}', align = 'right')
	pen.goto(0, (-HEIGHT / 2) - DIMENSIONS_OFFSET)
	pen.write(f'{shape.input_props["web_width"]["value"]} {shape.input_props["web_width"]["unit"]}', align = 'center')
	pen.goto((-web_width / 2) - DIMENSIONS_OFFSET, 0)
	pen.write(f'{shape.input_props["web_height"]["value"]} {shape.input_props["web_height"]["unit"]}', align = 'right')

	# Stop turtle from closing
	input('Press any key to continue')