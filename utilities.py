# Function used to check if a value is above 0
is_above_0 = lambda x: x > 0

# Function used to convert from property to string
def property_to_string(property):

	# Remove all underscores and capitalise the start of each word
	output = property.replace('_', ' ').title()

	# Return output string
	return output