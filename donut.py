# Imports
import shape
import math

# Derive from base shape class
class donut(shape.shape):

	# Override initialisation function
	def __init__(self, outer_radius = 0, inner_radius = 0, density = 0, beam_length = 0, elasticity = 0):

		# Declare rectangle properties
		properties = {
			'inner_radius'		: { 'value': inner_radius, 'unit': 'mm'},
			'outer_radius'		: { 'value': outer_radius, 'unit': 'mm'},
			'length'		: { 'value': beam_length, 'unit': 'm'},
			'density'		: { 'value': density, 'unit': 'kg/m^3'},
			'elasticity'		: { 'value': elasticity, 'unit': 'kN/m^2'},
		}

		# Create new rectangle object
		super().__init__(properties)

		# Set shape name
		self.name = 'Hollow Circular'


	# Function called to calculate shape properties
	def calculate_properties(self):

		# Calculate perimeter
		self.output_props['perimeter'] = { 'value': self.calculate_perimeter(), 'unit': 'mm' }

		# Calculate area
		self.output_props['area'] = { 'value': self.calculate_area(), 'unit': 'mm^2' }

		# Calculate inertia
		self.output_props['inertia'] = { 'value': self.calculate_inertia(), 'unit': 'mm^4' }

		# Call base function
		super().calculate_general_properties()

	# Function called to calculate perimeter
	def calculate_perimeter(self):
		
		# Extract data from input properties
		i = self.input_props['inner_radius']['value']
		o = self.input_props['outer_radius']['value']

		# Calculate perimeter
		perimeter = (2 * math.pi * i) + (2 * math.pi * o)

		# Return perimeter
		return perimeter

	# Function called to calculate area
	def calculate_area(self):

		# Extract data from input properties
		i = self.input_props['inner_radius']['value']
		o = self.input_props['outer_radius']['value']

		# Calculate area
		area = (math.pi * (o ** 2)) - (math.pi * (i ** 2))

		# Return area
		return area

	# Function called to calculate inertia
	def calculate_inertia(self):
		
		# Extract data from input properties
		i = self.input_props['inner_radius']['value']
		o = self.input_props['outer_radius']['value']

		# Calculate inertia
		inertia = (math.pi * ((2 * o) ** 4) - (2 * i) ** 4) / 64

		# Return inertia
		return inertia