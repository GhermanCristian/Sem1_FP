'''
Assignment 5 - due on 5 Nov 2019
Problem 1
    Manage a list of complex numbers in the a + bi form and provide the following features
    - add a number to the list (it is read from the console)
    - show the number list
    - filter the list so that it only contains only the numbers between indices startPos, endPos (they are
read from the console)
    - undo 
'''
from UI import UI
from Test import Test

def main():
    testing = Test()
    testing.testFunction()
    interface = UI()
    interface.menuInterface()

if __name__ == "__main__":
    main()