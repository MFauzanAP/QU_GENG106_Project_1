# Imports
import menu
import writing

# Declare function that will be called at startup
def main():
	
	
	# Declare dictionary of menu choices and their respective functions
	menu_choices = {
		1		: menu.ask_rectangle,
		2		: menu.ask_circle,
		3		: menu.ask_donut,
		4		: menu.ask_t_section,
		5		: menu.ask_i_section,
		6		: writing.new_entry, 
		7		: menu.show_prev,
		9		: exit,
	}

	# Infinite loop to keep asking question
	while True:

		# Ask the user for a shape and redirect to the shape
		menu_choices[menu.ask_shape()]()

# Call main function
main()