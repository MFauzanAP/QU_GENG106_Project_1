# Imports
import graphics

# Base shape class that will be overwritten to create the other classes
class shape:

	# Variable to hold the name of the shape
	name = 'Shape'

	# Dictionary used to hold the input properties of the shape
	input_props = {
		'dimensions' 		: { },
		'density'		: { },
		'elasticity'		: { }
	}

	# Dictionary used to hold the calculated properties of the shape
	output_props = {
		'perimeter'		: { },
		'area'			: { },
		'inertia'		: { },
		'surface area'		: { },
		'weight'		: { },
		'flexural rigidity'	: { }
	}



	# Declare lambda to calculate surface area
	calculate_surface_area = lambda self : (self.output_props['perimeter']['value'] / 1000) * self.input_props['length']['value']

	# Declare lambda to calculate weight
	calculate_weight = lambda self : (self.output_props['area']['value'] / 1000000) * self.input_props['length']['value'] * self.input_props['density']['value']

	# Declare lambda to calculate flexural rigidity
	calculate_flexural_rigidity = lambda self : self.input_props['elasticity']['value'] * (self.output_props['inertia']['value'] / 10000000000)
	# TODO show user what they are inputting


	# Function called to initialise the object
	def __init__(self, properties):

		# Set shape input properties
		self.input_props = properties.copy()

	# Function called to calculate the general properties of the shape
	def calculate_general_properties(self):

		# Calculate surface area
		self.output_props['surface area'] = { 'value': self.calculate_surface_area(), 'unit': 'm^2' }

		# Calculate weight
		self.output_props['weight'] = { 'value': self.calculate_weight(), 'unit': 'kg' }

		# Calculate flexural rigidity
		self.output_props['flexural rigidity'] = { 'value': self.calculate_flexural_rigidity(), 'unit': 'kN.m^2' }

	# Function called to print out the properties of the shape
	def print_properties(self):

		# Print out title
		graphics.print_shape(self)