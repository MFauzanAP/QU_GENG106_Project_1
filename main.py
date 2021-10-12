# Imports
import menu

# Declare function that will be called at startup
def main():

	# Declare dictionary of menu choices and their respective functions
	menu_choices = {
		1		: menu.ask_rectangle,
		2		: menu.ask_circle,
		3		: menu.ask_rectangle,
		4		: menu.ask_t_section,
		5		: menu.ask_rectangle,
		9		: exit
	}

	# Ask the user for a shape and redirect to the shape
	menu_choices[menu.ask_shape()]()

# Call main function
main()