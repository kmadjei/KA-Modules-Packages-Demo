def say_hello():
    """Sends a greeting to the user"""
    print("Hello Guest! Welcome to the Kenneth module \n")
    # prompt user to enter his/her name
    fname = input("What's your first name: ")
    lname = input("What's your Sur name: ")
    print(f"\nHi {fname} {lname}. I hope you enjoy this fun python module.\n")

def fizzBuzz_game():
    """Initiates Fizz Buzz game"""
    print("Welcome to the Fizz Buzz challenge game. Let's get started \n")
  
    
    while True:
        #gets user's number
        fb_number = input("Please enter any number divisible by 7 or 5: ")
        
        try:
            x = float(fb_number)
            #Validates user input
            if x % 7 == 0 and x % 5 == 0:
                print("Fizz Buzz!\n")
                play = input("Choose (y) if you want to continue or (n) to exit: ")
                if play.lower() == "y":
                    continue
                else:
                    return print("Thank You for playing the Fizz Buzz game!\n")
                
            elif x % 5 == 0:
                print("Fizz!")
                play = input("Choose (y) if you want to continue or (n) to exit: ")
                if play.lower() == "y":
                    continue
                else:
                    return print("Thank You for playing the Fizz Buzz game!\n")

            elif x % 7 == 0:
                print("Buzz!")
                play = input("Choose (y) if you want to continue or (n) to exit: ")
                if play.lower() == "y":
                    continue
                else:
                    return print("Thank You for playing the Fizz Buzz game!\n")

            else: 
                print("Sorry your number did not match any of the conditions.")
                print("Please try again.\n")
        except:
            print(f"Sorry {fb_number} is not a number. Try again!\n")

