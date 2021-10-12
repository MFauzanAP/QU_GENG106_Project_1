# Imports
import os
import math
import utilities
from prettytable import PrettyTable

# Function used to clear the screen
def clear_screen():

	# Clear screen
	os.system('cls||clear')

# Function used to output the properties of a shape
def print_shape(shape):

	# Clear screen
	clear_screen()

	# Store title in a variable
	title = f'{shape.name} Properties'

	# Print shape name and underline
	print(title)

	# Create new table
	table = PrettyTable(['Property', 'Value', 'Unit'])

	# Set column alignment
	table.align['Value'] = 'l'
	table.align['Unit'] = 'l'

	# Loop through each input property
	for prop in shape.input_props:

		# Get value from shape property
		value = f'{shape.input_props[prop]["value"]}'
		unit = f'{shape.input_props[prop]["unit"]}'

		# Calculate the number of digits it has
		digits = math.log10(abs(float(value))) if utilities.is_above_0(float(value)) else 0

		# Change to scientific notation if too many digits
		if digits >= 12: value = f'{shape.input_props[prop]["value"]:e}'

		# Print the name of the property and the value
		table.add_row([utilities.property_to_string(prop), value, unit])

	# Loop through each output property
	for prop in shape.output_props:

		# Get value from shape property
		value = f'{shape.output_props[prop]["value"]}'
		unit = f'{shape.output_props[prop]["unit"]}'

		# Calculate the number of digits it has
		digits = math.log10(abs(float(value))) if utilities.is_above_0(float(value)) else 0

		# Change to scientific notation if too many digits
		if digits >= 12: value = f'{shape.output_props[prop]["value"]:e}'

		# Print the name of the property and the value
		table.add_row([utilities.property_to_string(prop), value, unit])

	# Print table
	print(table)

# Function used to output the interface used to ask the user for shape properties
def print_ask_properties(shape):

	# Clear screen
	clear_screen()

	# Store title in a variable
	title = f'{shape.name} Properties'

	# Print shape name and underline
	print(title)

	# Create new table
	table = PrettyTable(['Property', 'Value', 'Unit'])

	# Set column alignment
	table.align['Value'] = 'l'
	table.align['Unit'] = 'l'

	# Loop through each input property
	for prop in shape.input_props:

		# Get value from shape property
		value = f'{shape.input_props[prop]["value"]}'
		unit = f'{shape.input_props[prop]["unit"]}'

		# Calculate the number of digits it has
		digits = math.log10(abs(float(value))) if utilities.is_above_0(float(value)) else 0

		# Change to scientific notation if too many digits
		if digits >= 12: value = f'{shape.input_props[prop]["value"]:e}'

		# Print the name of the property and the value
		table.add_row([utilities.property_to_string(prop), value, unit])

	# Output table
	print(table)

	# Enter a new line
	print()

# Function used to output menu
def print_menu():

	# Clear screen
	clear_screen()

	# Output title
	print(f'Geometric Shapes Application')

	# Output options
	print(f'(1) Rectangle')
	print(f'(2) Circle')
	print(f'(3) Donut')
	print(f'(4) T-Section')
	print(f'(5) I-Section')
	print()
	print(f'(9) Exit')
	print()