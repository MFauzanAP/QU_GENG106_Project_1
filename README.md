# QU_GENG106_Project_1
Source code for the first computer programming 106 project at Qatar University

## shape.py
Abstract class used as a basis for all the other shape classes

### Properties
- `name` - Stores the name of the shape. This variable will be set in the initialisation function of each shape class.
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
- `input_props` - A dictionary that stores the input properties of a shape. Examples of this are dimensions, density, and elasticity
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
- `output_props` - A dictionary that stores the output properties of a shape. Examples of this are volume, weight, and surface area
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
- `__init__(properties)` - Used to initialise a new shape, mainly used in the initialisation function of a class
	 - **Parameters**
	 	 - `properties` - A dictionary containing all the input properties

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
	 - **Returns**
		 - No returns
- `print_properties()` - Used to print all of a shapes properties as long as they are in the input and output props variable.
	 - **Parameters**
	 	 - No parameters
	 - **Returns**
	 	 - No returns
	 - **Example Output**
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
