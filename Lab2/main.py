'''
Assignment 2 - due on 15 Oct 2019
sequences 
    - 3 = nr. having the same modulus
    - 8 = nr. with (0 <= modulus <= 10)
    - (in-Lab) 12 = nr. that can be written using the same base 10 digits
'''

from setData import readList
from getData import printList
from menuUI import displayMenu, getUserChoice
from sequences import firstSequence, secondSequence, thirdSequence

def main():
    running = True
    #nrList = [(2.46, 5.01), (3.15, 4.11), (7.03, 8.42), (3.11, 3.08), (1.95, 5.30), (7.05, 7.25), (5.76, 5.56), (5.34, 5.74), (0.85, 8.65), (6.56, 2.05)]
    nrList = [(0, 1), (1, 2), (2, 1), (-2, 1), (10, 2.2), (10, 2.2), (10, 2.2), (0, 0), (1, 2), (2, 1)]
    #nrList = [(22122, 12), (1, 2), (2, 1), (-2, 1), (10, 2), (10, 2), (10, 2), (0, 120), (10, 2), (2, 1)]
    while running:
        displayMenu()
        choice = getUserChoice()
        if choice == 1:
            nrList = readList()
        elif choice == 2:
            printList(nrList)
        elif choice == 3:
            print ("\nSame modulus: ")
            printList(firstSequence(nrList))
        elif choice == 4:
            print ("\nModulus in range [0, 10]: ")
            printList(secondSequence(nrList))
        elif choice == 5:
            print ("\nNumbers that can be written using the same base 10 digits: ")
            printList(thirdSequence(nrList))
        elif choice == 6:
            print ("\nProgram ended")
            running = False

if __name__ == "__main__":
    main()