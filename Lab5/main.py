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
from newUI import newUI
from Test import Test

def getUIChoice():
    while True:
        x = input("Insert UI Choice: \n")
        try:
            x = int(x)
        except:
            continue
        if x == 1:
            return UI()
        return newUI()

def main():
    testing = Test()
    testing.testFunction()
    interface = getUIChoice()
    interface.menuInterface()

if __name__ == "__main__":
    main()