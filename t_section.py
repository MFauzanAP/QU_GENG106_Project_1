# Imports
import shape

# Derive from base shape class
class t_section(shape.shape):
	
	# Declare lambda to calculate perimeter
	calculate_perimeter = lambda self : (2 * self.input_props['flange_width']['value']) + (2 * self.input_props['flange_height']['value']) + (2 * self.input_props['web_height']['value'])

	# Declare lambda to calculate area
	calculate_area = lambda self : (self.input_props['flange_width']['value'] * self.input_props['flange_height']['value']) + (self.input_props['web_width']['value'] * self.input_props['web_height']['value'])



	# Override initialisation function
	def __init__(self, overall_width, overall_height, flange_width, flange_height, web_width, web_height, length, density, elasticity):

		# Declare rectangle properties
		properties = {
			'overall_width'		: { 'value': overall_width, 'unit': 'mm'},
			'overall_height'	: { 'value': overall_height, 'unit': 'mm'},
			'flange_width'		: { 'value': flange_width, 'unit': 'mm'},
			'flange_height'		: { 'value': flange_height, 'unit': 'mm'},
			'web_width'		: { 'value': web_width, 'unit': 'mm'},
			'web_height'		: { 'value': web_height, 'unit': 'mm'},
			'length'		: { 'value': length, 'unit': 'm'},
			'density'		: { 'value': density, 'unit': 'kg/m^3'},
			'elasticity'		: { 'value': elasticity, 'unit': 'kN/m^2'}
		}

		# Create new t_section object
		super().__init__(properties)

		# Set shape name
		self.name = 'T Section'

		# Calculate shape properties
		self.calculate_properties()

		# Print properties
		self.print_properties()

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

	# Function called to calculate inertia
	def calculate_inertia(self):
        
		# Extract data from input properties
		b = self.input_props['overall_width']['value']
		d = self.input_props['overall_height']['value']
		s = self.input_props['flange_height']['value']
		t = self.input_props['web_width']['value']
		h = self.input_props['web_height']['value']

		# Calculate numerator
		numerator = ((d ** 2) * t) + ((s ** 2) * (b - t))

		# Calculate denominator
		denominator = (2 * ((b * s) + (h * t)))

		# Calculate y
		y = d - (numerator / denominator)
  
		# Calculate inertia
		inertia = (t * (y ** 3) + (b * ((d - y) ** 3)) - ((b - t) * ((d - y - s) ** 3))) / 3

		# Return inertia
		return inertia