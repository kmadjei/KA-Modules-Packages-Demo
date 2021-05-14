# import module 
import kenneth_module

# init colorama objects Style, Fore and Back
# to change text color and background color 
from colorama import  Fore, Back, Style


# using the background and text color properties of the colorama package
print(f" {Back.YELLOW} {Fore.RED} Hello Everyone. I am Colorama from the Python Package Index\n")

# change the styles back to normal
print(Style.RESET_ALL)

# make the terminal font color yellow
print(Fore.YELLOW )

# accessing module functions
kenneth_module.say_hello()
kenneth_module.fizzBuzz_game()

# change the styles back to normal
print(Style.RESET_ALL)