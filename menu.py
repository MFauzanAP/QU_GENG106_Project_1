# Imports
import graphics
from rectangle import rectangle
from circle import circle
from t_section import t_section
from i_section import i_section
from donut import donut
import utilities
import math
import writing
import drawing



# Function used to ask user which shape he wants
def ask_shape():

	# Ask user to choose a shape and validate it and then return the users choice
	return validate_input(graphics.print_menu, 'Enter Your Choice: ', legal = [1, 2, 3, 4, 5, 6, 7, 9])

# Function used to ask the user for rectangle data
def ask_rectangle():

	# Create a new rectangle with starting values
	shape = rectangle()

	# Ask user to enter rectangle properties
	shape.input_props['width']['value'] = validate_input(graphics.print_ask_properties, 'Enter Rectangle Width: ', args = shape)
	shape.input_props['height']['value'] = validate_input(graphics.print_ask_properties, 'Enter Rectangle Height: ', args = shape)
	shape.input_props['length']['value'] = validate_input(graphics.print_ask_properties, 'Enter Beam Length: ', args = shape)
	shape.input_props['density']['value'] = validate_input(graphics.print_ask_properties, 'Enter Rectangle Density: ', args = shape)
	shape.input_props['elasticity']['value'] = validate_input(graphics.print_ask_properties, 'Enter Rectangle Elasticity: ', args = shape)

	# Append to the file
	writing.written('Rectangle', '---')
	writing.written('width', shape.input_props['width']['value'])
	writing.written('height', shape.input_props['height']['value'])
	writing.written('beam length', shape.input_props['length']['value'])
	writing.written('density', shape.input_props['density']['value'])
	writing.written('elasticity', shape.input_props['elasticity']['value'])

	# Recalculate properties
	shape.calculate_properties()

	# Print out rectangle properties
	shape.print_properties()

	# Draw rectangle using matlplotlib
	drawing.draw_rectangle(shape.input_props['width']['value'],shape.input_props['height']['value'])

	# Ending the entry
	writing.end_entry()

# Function used to ask the user for circle data
def ask_circle():

	# Create a new circle with starting values
	shape = circle()

	# Ask user to enter circle properties
	shape.input_props['radius']['value'] = validate_input(graphics.print_ask_properties, 'Enter Circle Radius: ', args = shape)
	shape.input_props['length']['value'] = validate_input(graphics.print_ask_properties, 'Enter Beam Length: ', args = shape)
	shape.input_props['density']['value'] = validate_input(graphics.print_ask_properties, 'Enter Circle Density: ', args = shape)
	shape.input_props['elasticity']['value'] = validate_input(graphics.print_ask_properties, 'Enter Circle Elasticity: ', args = shape)

	# Append to the file 
	writing.written('Circular','---')
	writing.written('radius', shape.input_props['radius']['value'])
	writing.written('beam length', shape.input_props['length']['value'])
	writing.written('density', shape.input_props['density']['value'])
	writing.written('elasticity', shape.input_props['elasticity']['value'])

	# Recalculate properties
	shape.calculate_properties()

	# Print out circle properties
	shape.print_properties()
 
	# Draw circle using turtle
	drawing.draw_circle(shape.input_props['radius']['value'])

	# Ending the entry
	writing.end_entry()

# Function used to ask the user for donut data
def ask_donut():

	# Create a new donut with starting values
	shape = donut()

	# Ask user to enter donut properties
	shape.input_props['outer_radius']['value'] = validate_input(graphics.print_ask_properties, 'Enter Outer Radius: ', args = shape)
	shape.input_props['inner_radius']['value'] = validate_input(graphics.print_ask_properties, 'Enter Inner Radius: ', args = shape, max = shape.input_props['outer_radius']['value'])
	shape.input_props['length']['value'] = validate_input(graphics.print_ask_properties, 'Enter Beam Length: ', args = shape)
	shape.input_props['density']['value'] = validate_input(graphics.print_ask_properties, 'Enter Hollow Circular Density: ', args = shape)
	shape.input_props['elasticity']['value'] = validate_input(graphics.print_ask_properties, 'Enter Hollow Circular Elasticity: ', args = shape)

	# Append to the file 
	writing.written('Hollow Circular','---')
	writing.written('outer radius', shape.input_props['outer_radius']['value'])
	writing.written('inner radius', shape.input_props['inner_radius']['value'])
	writing.written('beam length', shape.input_props['length']['value'])
	writing.written('density', shape.input_props['density']['value'])
	writing.written('elasticity', shape.input_props['elasticity']['value'])

	# Recalculate properties
	shape.calculate_properties()

	# Print out circle properties
	shape.print_properties()

	# Draw donut using matplotlib
	drawing.draw_donut(shape.input_props['outer_radius']['value'], shape.input_props['inner_radius']['value'])

	# Ending the entry
	writing.end_entry()

# Function used to ask the user for t section data
def ask_t_section():

	# Create a new t_section with starting values
	shape = t_section()

	# Ask user to enter t_section properties
	shape.input_props['flange_width']['value'] = validate_input(graphics.print_ask_properties, 'Enter Flange Width: ', args = shape)
	shape.input_props['flange_height']['value'] = validate_input(graphics.print_ask_properties, 'Enter Flange Height: ', args = shape)
	shape.input_props['web_width']['value'] = validate_input(graphics.print_ask_properties, 'Enter Web Width: ', args = shape, max = shape.input_props['flange_width']['value'])
	shape.input_props['web_height']['value'] = validate_input(graphics.print_ask_properties, 'Enter Web Height: ', args = shape)
	shape.input_props['length']['value'] = validate_input(graphics.print_ask_properties, 'Enter Beam Length: ', args = shape)
	shape.input_props['density']['value'] = validate_input(graphics.print_ask_properties, 'Enter T Section Density: ', args = shape)
	shape.input_props['elasticity']['value'] = validate_input(graphics.print_ask_properties, 'Enter T Section Elasticity: ', args = shape)

	# Append to the file
	writing.written('T-section','---')
	writing.written('flange width', shape.input_props['flange_width']['value'])
	writing.written('flange height', shape.input_props['flange_height']['value'])
	writing.written('web_width',shape.input_props['web_width']['value'])
	writing.written('web_height',shape.input_props['web_height']['value'])
	writing.written('beam length', shape.input_props['length']['value'])
	writing.written('density', shape.input_props['density']['value'])
	writing.written('elasticity', shape.input_props['elasticity']['value'])

	# Recalculate properties
	shape.calculate_properties()

	# Print out t_section properties
	shape.print_properties()

	# Draw t_section using matplotlib
	drawing.draw_t_section(shape.input_props['web_width']['value'],shape.input_props['web_height']['value'],shape.input_props['flange_width']['value'],shape.input_props['flange_height']['value'])

	# Ending the entry
	writing.end_entry()

# Function used to ask the user for i section data
def ask_i_section():

	# Create a new t_section with starting values
	shape = i_section()

	# Ask user to enter t_section properties
	shape.input_props['flange_width']['value'] = validate_input(graphics.print_ask_properties, 'Enter Flange Width: ', args = shape)
	shape.input_props['flange_height']['value'] = validate_input(graphics.print_ask_properties, 'Enter Flange Height: ', args = shape)
	shape.input_props['web_width']['value'] = validate_input(graphics.print_ask_properties, 'Enter Web Width: ', args = shape, max = shape.input_props['flange_width']['value'])
	shape.input_props['web_height']['value'] = validate_input(graphics.print_ask_properties, 'Enter Web Height: ', args = shape)
	shape.input_props['length']['value'] = validate_input(graphics.print_ask_properties, 'Enter Beam Length: ', args = shape)
	shape.input_props['density']['value'] = validate_input(graphics.print_ask_properties, 'Enter I Section Density: ', args = shape)
	shape.input_props['elasticity']['value'] = validate_input(graphics.print_ask_properties, 'Enter I Section Elasticity: ', args = shape)

	# Append to the file
	writing.written('I-Section','---')
	writing.written('flange width', shape.input_props['flange_width']['value'])
	writing.written('flange height', shape.input_props['flange_height']['value'])
	writing.written('web_width',shape.input_props['web_width']['value'])
	writing.written('web_height',shape.input_props['web_height']['value'])
	writing.written('beam length', shape.input_props['length']['value'])
	writing.written('density', shape.input_props['density']['value'])
	writing.written('elasticity', shape.input_props['elasticity']['value'])

	# Recalculate properties
	shape.calculate_properties()

	# Print out t_section properties
	shape.print_properties()

	# Draw t_section using matplotlib
	drawing.draw_i_section(shape.input_props['web_width']['value'],shape.input_props['web_height']['value'],shape.input_props['flange_width']['value'],shape.input_props['flange_height']['value'])

	# Ending the entry
	writing.end_entry()

# show the contents of the file
def show_prev(): 
	writing.get_previous()
	input()


# Function used to validate user input
def validate_input(function, message, legal = [], args = None, min = -math.inf, max = math.inf):

	# Declare variable to store error message
	error = ''

	# Infinite loop to handle validation of user input
	while True:

		# Try to ask the user for a shape
		try:

			# Call function
			function(args) if args is not None else function()

			# Print error message if there is
			if error: print(error)

			# Ask user a question and store their response
			response = float(input(message))

			# Gets legal list from parameter if present, else then creates a new list with the response since all responses are legal
			final_legal = [ response ] if len(legal) == 0 else legal

			# Restart loop if value is negative
			if not utilities.is_above_0(response): 

				# Set error message
				error = 'Input cannot be negative or 0'
				
				# Restart loop
				continue

			# Restart loop if value is below minimum
			if response <= min:

				# Set error message
				error = f'Input cannot be equal to or below {min}'
				
				# Restart loop
				continue

			# Restart loop if value is below minimum
			if response >= max:

				# Set error message
				error = f'Input cannot be equal to or above {max}'
				
				# Restart loop
				continue

			# If user input is legal then continue
			if response in final_legal:

				# Reset error message
				error = ''

				# Break out of loop
				break

			# If user input is illegal then restart loop and pass error
			else:

				# Set error message
				error = f'Input must be legal = {legal}'
				
				# Restart loop
				continue

		# If there is an error
		except ValueError:

			# Pass error message to user
			error = 'Input is not a number'

			# Restart loop
			continue

	# Return the user input
	return response