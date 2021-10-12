# Imports
import shape
import math
# Derive from base shape class
class circle(shape.shape):

	# Override initialisation function
	def __init__(self, radius = 0, length = 0, density = 0, elasticity = 0):

		# Declare rectangle properties
		properties = {
		'web_depth'		: { 'value': web_depth, 'unit': 'mm'},
		'web_height'		: { 'value': web_height, 'unit': 'mm'},
		'web_width'		: { 'value': web_width, 'unit': 'mm'},
		'flange_width'		: { 'value': flange_width, 'unit': 'mm'},
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

		# Calculate area
		self.output_props['area'] = { 'value': self.calculate_area(), 'unit': 'mm^2' }

		# Call base function
		super().calculate_general_properties()
		
	# Function called to calculate area
	def calculate_area(self):

		# Extract data from input properties
		r = self.input_props['radius']['value']

		# Calculate area
		area = math.PI * (r ** 2)

		# Return area
		return area

