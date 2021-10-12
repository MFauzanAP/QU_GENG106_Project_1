# QU_GENG106_Project_1
Source code for the first computer programming 106 project at Qatar University

## Instructions
1. Clone this repository onto your local machine
2. Open the folder where you installed the project in VS Code
4. Open the `main.py` file and press start

## Creating a New Shape
1. Create a new file for your shape. You can call this file whatever you want. eg `circle.py`
2. Copy paste this example script, then change the class name to whatever shape you're making.
	```
	# Imports
	import shape

	# Derive from base shape class
	class circle(shape.shape):

		# Override initialisation function
		def __init__(self):

			# Declare rectangle properties
			properties = {
				'length'		: { 'value': length, 'unit': 'm'},
				'density'		: { 'value': density, 'unit': 'kg/m^3'},
				'elasticity'		: { 'value': elasticity, 'unit': 'kN/m^2'},
			}

			# Create new rectangle object
			super().__init__(properties)

			# Set shape name
			self.name = 'Circle'

			# Calculate shape properties
			self.calculate_properties()

			# Print properties
			self.print_properties()

		# Function called to calculate shape properties
		def calculate_properties(self):

			# Call base function
			super().calculate_general_properties()
	```
3. Add in your shape's properties and add them to the `properties` variable inside the `__init__` function like so:
	```
	# Override initialisation function
	def __init__(self, radius, length, density, elasticity):

		# Declare rectangle properties
		properties = {
			'radius'		: { 'value': width, 'unit': 'mm'},
			'length'		: { 'value': length, 'unit': 'm'},
			'density'		: { 'value': density, 'unit': 'kg/m^3'},
			'elasticity'		: { 'value': elasticity, 'unit': 'kN/m^2'},
		}

		# Create new rectangle object
		super().__init__(properties)

		# Set shape name
		self.name = 'Circle'

		# Calculate shape properties
		self.calculate_properties()

		# Print properties
		self.print_properties()
	```
4. Add your shape's calculations using lambdas and call them in the `calculate_properties` function. Then add the calculated property to the shape's `output_props` variable like so:
	```
	# Declare lambda to calculate area
	calculate_area = lambda self : math.PI * (self.input_props['radius']['value'] ** 2)
	
	# Function called to calculate shape properties
	def calculate_properties(self):

		# Calculate area
		self.output_props['area'] = { 'value': self.calculate_area(), 'unit': 'mm^2' }

		# Call base function
		super().calculate_general_properties()
	```
5. Now open the `menu.py` file and import your shape at the top. Then copy paste this function and add your shape's input properties in like so:
	```
	# Function used to ask the user for circle data
	def ask_circle():

		# Create a new circle with starting values
		circle = circle.circle(0, 0, 0, 0)

		# Ask user to enter circle properties
		circle.input_props['radius']['value'] = validate_input(graphics.print_ask_properties, 'Enter Circle Radius: ', args = circle)
		circle.input_props['length']['value'] = validate_input(graphics.print_ask_properties, 'Enter Circle Length: ', args = circle)
		circle.input_props['density']['value'] = validate_input(graphics.print_ask_properties, 'Enter Circle Density: ', args = circle)
		circle.input_props['elasticity']['value'] = validate_input(graphics.print_ask_properties, 'Enter Circle Elasticity: ', args = circle)

		# Recalculate properties
		circle.calculate_properties()

		# Print out circle properties
		circle.print_properties()
	```
6. Now open `main.py` and add in your newly made function to the dictionary like so:
	```
	menu_choices = {
		1		: menu.ask_rectangle,
		2		: menu.ask_circle,
		9		: exit
	}
	```

## shape.py
Abstract class used as a basis for all the other shape classes

### Properties
- #### `name` 
	 - Stores the name of the shape. This variable will be set in the initialisation function of each shape class.
	 - Setting the name of the shape
	```
	# rectangle.py
	# Override initialisation function
	def __init__(self):

		# Set shape name
		self.name = 'Rectangle'
	```
	 - Getting the name of the shape
	 ```
	 # Create a new rectangle
	 rect = rectangle.rectangle()

	 # Get the name of the shape
	 name = rect.name
	 ```

- #### `input_props`
	 - A dictionary that stores the input properties of a shape. Examples of this are dimensions, density, and elasticity
	 - Each value must be another dictionary that contains a keys for the value of the property as well as its unit
	 ```
	 input_props = {
		'width' : { 
			'value': 10, 
			'unit': 'm' 
		},
		'density': { 
			'value': 5, 
			'unit': 'kg/m^3' 
		},
		'elasticity': { 
			'value': 1, 
			'unit': 'kN/m^2' 
		}
	}
	 ```
	 - Value key of each property will be used for calculations
	 - Unit key of each property will be used for printing and output

- #### `output_props`
	 - A dictionary that stores the output properties of a shape. Examples of this are volume, weight, and surface area
	 - Each value must be another dictionary that contains a keys for the value of the property as well as its unit
	 ```
	 output_props = {
		'volume' : { 
			'value': 10, 
			'unit': 'm^3' 
		},
		'weight': { 
			'value': 5, 
			'unit': 'kg' 
		},
		'surface area': { 
			'value': 1, 
			'unit': 'm^2' 
		}
	}
	 ```
	 - Value key of each property will be used for calculations
	 - Unit key of each property will be used for printing and output

### Functions
- #### `__init__(properties)`
	 - Used to initialise a new shape, mainly used in the initialisation function of a class
	 - ##### Parameters
	 	 - `properties`
			 - A dictionary containing all the input properties
			 - **Type** - Dictionary
			 ```
			 properties = {
				 'width'	: { 
					 'value': width, 
					 'unit': 'm'
				 },
				 'density': { 
					 'value': density, 
					 'unit': 'kg/m^3'
				 },
				 'elasticity': { 
					 'value': elasticity, 
					 'unit': 'kN/m^2'
				 },
			 }
			 ```
	 - ##### Returns
		 - Returns the newly created shape object

- #### `print_properties()`
	 - Used to print all of a shapes properties as long as they are in the input and output props variable.
	 - ##### Parameters
		 - No parameters
	 - ##### Returns
		 - No returns
	 - ##### Example Output
	 ```
	 Rectangle Properties
	 width = 10 m
	 height = 10 m
	 length = 10 m
	 density = 10 kg/m^3
	 elasticity = 10 kN/m^2

	 perimeter = 40 m
	 area = 100 m^2
	 inertia = 833.3333333333334 m^4
	 surface area = 400 m^2
	 weight = 10000 kg
	 flexural rigidity = 8333.333333333334 kN.m^2
	 ```

## rectangle.py
Class derived from the shape base class, one of the options for the menu

### Properties
- This class has no properties

### Functions
- #### `__init__(width, height, length, density, elasticity)`
	 - Creates a new rectangle class with the given parameters, and then calculates the output properties
	 - ##### Parameters
		 - `width`
			 - The rectangles width
			 - **Type** - Float / Int
		 - `height`
			 - The rectangles height
			 - **Type** - Float / Int
		 - `length`
			 - The rectangles length
			 - **Type** - Float / Int
		 - `density`
			 - The rectangles density
			 - **Type** - Float / Int
		 - `elasticity`
			 - The rectangles elasticity
			 - **Type** - Float / Int
	 - ##### Returns
		 - Returns the newly created rectangle object
- #### `calculate_properties()`
	 - Calculates the rectangles output properties like perimeter, area, inertia, surface area, weight, and flexural rigidity
	 - ##### Parameters
		 - No parameters
	 - ##### Returns
		 - No returns
- #### `calculate_perimeter()`
	 - Calculates the rectangles perimeter
	 - ##### Parameters
		 - No parameters
	 - ##### Returns
		 - Returns the calculated perimeter
- #### `calculate_area()`
	 - Calculates the rectangles area
	 - ##### Parameters
		 - No parameters
	 - ##### Returns
		 - Returns the calculated area
- #### `calculate_inertia()`
	 - Calculates the rectangles inertia
	 - ##### Parameters
		 - No parameters
	 - ##### Returns
		 - Returns the calculated inertia
- #### `calculate_surface_area()`
	 - Calculates the rectangles surface area
	 - ##### Parameters
		 - No parameters
	 - ##### Returns
		 - Returns the calculated surface area
- #### `calculate_weight()`
	 - Calculates the rectangles weight
	 - ##### Parameters
		 - No parameters
	 - ##### Returns
		 - Returns the calculated weight
- #### `calculate_flexural_rigidity()`
	 - Calculates the rectangles flexural rigidity
	 - ##### Parameters
		 - No parameters
	 - ##### Returns
		 - Returns the calculated flexural rigidity
