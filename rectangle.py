# Imports
import shape

# Derive from base shape class
class rectangle(shape.shape):

	# Override initialisation function
	def __init__(self, width = 0, height = 0, length = 0, density = 0, elasticity = 0):

		# Declare rectangle properties
		properties = {
			'width'			: { 'value': width, 'unit': 'mm'},
			'height'		: { 'value': height, 'unit': 'mm'},
			'length'		: { 'value': length, 'unit': 'm'},
			'density'		: { 'value': density, 'unit': 'kg/m^3'},
			'elasticity'		: { 'value': elasticity, 'unit': 'kN/m^2'},
		}

		# Create new rectangle object
		super().__init__(properties)

		# Set shape name
		self.name = 'Rectangle'

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
		b = self.input_props['width']['value']
		h = self.input_props['height']['value']

		# Calculate perimeter
		perimeter = (b * 2) + (h * 2)

		# Return perimeter
		return perimeter

	# Function called to calculate area
	def calculate_area(self):

		# Extract data from input properties
		b = self.input_props['width']['value']
		h = self.input_props['height']['value']

		# Calculate area
		area = b * h

		# Return area
		return area

	# Function called to calculate inertia
	def calculate_inertia(self):
        
		# Extract data from input properties
		b = self.input_props['width']['value']
		h = self.input_props['height']['value']

		# Calculate numerator
		numerator = b * (h ** 3)

		# Calculate inertia
		inertia = numerator / 12

		# Return inertia
		return inertia