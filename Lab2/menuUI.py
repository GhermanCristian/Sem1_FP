def displayMenu():
    '''
    Displays a menu-driven user interface
    Input:
        - none
    Output:
        - a list of options for the user to choose from
    '''
    print ("1. Read a list of complex numbers")
    print ("2. Display the list")
    print ("3. Display list sequence - same modulus")
    print ("4. Display list sequence - modulus in range [0, 10]")
    print ("5. (in-Lab)Display list sequence - numbers can be written using the same base 10 digits")
    print ("6. Exit program")

def getUserChoice():
    '''
    Determines the option chosen by the user. Ensures that it is a numeric value
    Input:
        - None
    Output:
        - an integer representing the choice ID
    '''
    found = False
    while not found:
        x = input("> ")
        try:
            x = int(x)
            if x in range(1, 7):
                found = True
            else:
                print ("No task with this ID. Try again")
        except:
            print ("Value is not an integer. Try again")
    return x
