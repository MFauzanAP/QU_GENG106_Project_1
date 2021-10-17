# Imports
import shape
import math

# Derive from base shape class
class circle(shape.shape):

	# Override initialisation function
	def __init__(self, radius = 0, diameter = 0, length = 0, density = 0 ,elasticity = 0):

		# Declare rectangle properties
		properties = {
			'radius'		: { 'value': radius, 'unit': 'mm'},
			'diameter'		: { 'value': diameter, 'unit': 'mm'},
			'length'		: { 'value': length, 'unit': 'm'},
			'density'		: { 'value': density, 'unit': 'kg/m^3'},
			'elasticity'		: { 'value': elasticity, 'unit': 'kN/m^2'},
		}

		# Create new rectangle object
		super().__init__(properties)

		# Set shape name
		self.name = 'Circle'

	# Function called to calculate shape properties
	def calculate_properties(self):
        
		# Calculate diameter
		self.input_props['diameter']['value'] = 2 * self.input_props['radius']['value']

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
		d = self.input_props['diameter']['value']

		# Calculate perimeter
		perimeter = math.pi * d

		# Return perimeter
		return perimeter

	# Function called to calculate area
	def calculate_area(self):

		# Extract data from input properties
		r = self.input_props['radius']['value']

		# Calculate area
		area = math.pi * (r ** 2)

		# Return area
		return area

	# Function called to calculate inertia
	def calculate_inertia(self):
        
		# Extract data from input properties
		d = self.input_props['diameter']['value']

		# Calculate numerator
		numerator = math.pi * (d ** 4)

		# Calculate inertia
		inertia = numerator / 64

		# Return inertia
		return inertia