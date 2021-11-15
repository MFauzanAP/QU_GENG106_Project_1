# Imports
import shape
import math
import writing

# Derive from base shape class
class donut(shape.shape):

	# Override initialisation function
	def __init__(self, outer_radius = 0, inner_radius = 0, density = 0, beam_length = 0, elasticity = 0):

		# Declare rectangle properties
		properties = {
			'outer_diameter'	: { 'value': inner_radius, 'unit': 'mm'},
			'inner_diameter'	: { 'value': inner_radius, 'unit': 'mm'},
			'outer_radius'		: { 'value': outer_radius, 'unit': 'mm'},
			'inner_radius'		: { 'value': inner_radius, 'unit': 'mm'},
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
         
		# Calculate outer diameter
		self.input_props['outer_diameter']['value'] = 2 * self.input_props['outer_radius']['value']
		writing.written('outer diameter', self.input_props['outer_diameter']['value'])
  
		# Calculate inner diameter
		self.input_props['inner_diameter']['value'] = 2 * self.input_props['inner_radius']['value']
		writing.written('inner diameter', self.input_props['inner_diameter']['value'])

		# Calculate perimeter
		self.output_props['perimeter'] = { 'value': self.calculate_perimeter(), 'unit': 'mm' }
		writing.written('perimeter',self.calculate_perimeter())

		# Calculate area
		self.output_props['area'] = { 'value': self.calculate_area(), 'unit': 'mm^2' }
		writing.written('area',self.calculate_area())

		# Calculate inertia
		self.output_props['inertia'] = { 'value': self.calculate_inertia(), 'unit': 'mm^4' }
		writing.written('inertia',self.calculate_inertia())

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
		di = self.input_props['inner_diameter']['value']
		d = self.input_props['outer_diameter']['value']

		# Calculate inertia
		inertia = (math.pi / 64) * ((d ** 4) - (di ** 4))

		# Return inertia
		return inertia