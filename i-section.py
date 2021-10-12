# Imports
import shape
import math
# Derive from base shape class
class i_section(shape.shape):

	# Override initialisation function
	def __init__(self,overall_depth=0,web_height=0,web_width=0,flange_width=0, length = 0, density = 0, elasticity = 0):

		# Declare rectangle properties
		properties = {
		'overall_depth'		: { 'value': overall_depth, 'unit': 'mm'},
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
		self.name = 'I-Section'


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
	def calculate_perimeter(self):
		length = self.input_props['length']['value']
		flange_width = self.input_props['flange_width']['value']
		web_width = self.input_props['web_width']['value']

		perimeter=2*((2*flange_width)+length-web_width)
    		
		return perimeter
	def calculate_secondMomentInertia(self):
		length = self.input_props['length']['value']
		flange_width = self.input_props['flange_width']['value']
		web_width = self.input_props['web_width']['value']
		web_height = self.input_props['web_height']['value']
		
		second_moment_inertia=((flange_width*(length**3))-2*((flange_width-web_width)/(2))*(web_height)**3)/(12)
		
		return second_moment_inertia
	def calculate_area(self):
		flange_width = self.input_props['flange_width']['value']
		web_width = self.input_props['web_width']['value']
		web_height = self.input_props['web_height']['value']

		area=(2*web_width*web_height)+(web_height*web_width)

		return area
	def calculate_surfaceArea(self):
		length = self.input_props['length']['value']
		flange_width = self.input_props['flange_width']['value']
		web_width = self.input_props['web_width']['value']
		web_height = self.input_props['web_height']['value']

		surfaceArea=(flange_width*length)-web_height*(flange_width-web_width)
	
	def calculate_beamWeight(self):
		overall_depth = self.input_props['overall_depth']['value']
		length = self.input_props['length']['value']
		flange_width = self.input_props['flange_width']['value']
		web_width = self.input_props['web_width']['value']
		web_height = self.input_props['web_height']['value']
		density = self.input_props['density']['value']
		
		beamVolume=(length*overall_depth*flange_width)-(2*((flange_width/2)-(web_width)/2)*(web_height)*(overall_depth))

		beamWeight=beamVolume*density
		
		return beamWeight
	def calculate_surfaceArea(self):
		length = self.input_props['length']['value']
		flange_width = self.input_props['flange_width']['value']
		web_width = self.input_props['web_width']['value']
		#There might be a better way to recall Perimeter.
		perimeter=2*((2*flange_width)+length-web_width)

		surfaceArea=length*perimeter
		
		return surfaceArea
	def calculate_flexuralRigidity(self):
		length = self.input_props['length']['value']
		flange_width = self.input_props['flange_width']['value']
		web_width = self.input_props['web_width']['value']
		web_height = self.input_props['web_height']['value']
		elasticity = self.input_props['elasticity']['value']
		#There might be a better way to recall Inertia.
		second_moment_inertia=((flange_width*(length**3))-2*((flange_width-web_width)/(2))*(web_height)**3)/(12)

		flexuralRigidity=second_moment_inertia*elasticity
		
		return flexuralRigidity


