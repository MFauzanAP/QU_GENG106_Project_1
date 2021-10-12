# Imports
import graphics
import turtle_graphics
import rectangle
import utilities

# Function used to ask user which shape he wants
def ask_shape():

	# Ask user to choose a shape and validate it and then return the users choice
	return validate_input(graphics.print_menu, 'Enter Your Choice: ', legal = [1, 2, 3, 4, 5, 9])

# Function used to ask the user for rectangle data
def ask_rectangle():

	# Create a new rectangle with starting values
	rect = rectangle.rectangle(0, 0, 0, 0, 0)

	# Ask user to enter rectangle properties
	rect.input_props['width']['value'] = validate_input(graphics.print_ask_properties, 'Enter Rectangle Width: ', args = rect)
	rect.input_props['height']['value'] = validate_input(graphics.print_ask_properties, 'Enter Rectangle Height: ', args = rect)
	rect.input_props['length']['value'] = validate_input(graphics.print_ask_properties, 'Enter Rectangle Length: ', args = rect)
	rect.input_props['density']['value'] = validate_input(graphics.print_ask_properties, 'Enter Rectangle Density: ', args = rect)
	rect.input_props['elasticity']['value'] = validate_input(graphics.print_ask_properties, 'Enter Rectangle Elasticity: ', args = rect)

	# Recalculate properties
	rect.calculate_properties()

	# Print out rectangle properties
	rect.print_properties()

	# Draw rectangle using turtle
	# turtle_graphics.setup_turtle()
	# turtle_graphics.draw_rectangle(rect)

# Function used to validate user input
def validate_input(function, message, legal = [], args = None):

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