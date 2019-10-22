#lab1 - extra - ex 11 from set 2, assignment 1
'''
The  numbers n1 and n2 have  the  property P if  their  writing  in base10 uses
the  same  digits (e.g. 2113 and 323121). Determine whether two given natural numbers have property P.
'''

#checks if n1 and n2 (integers) have the property P (same digits in base 10)
#the function returns True if they do, False otherwise
def haveProperty(n1, n2):
    #initialize digit lists
    digits1 = [False] * 10
    digits2 = [False] * 10
    
    #fill lists with the nr of appearances of each digit in n1, n2 respectively
    while n1:
        digits1[n1 % 10] = True
        n1 //= 10
    while n2:
        digits2[n2 % 10] = True
        n2 //= 10
        
    #checks if the lists have the same content
    for i in range(10):
        if digits1[i] != digits2[i]:
            return False
        
    #no differences were found, so the values have that property
    return True

if __name__ == "__main__":
    #version 1, maybe I could do sth cleaner
    '''
    running = True
    while running:
        x = input("Please insert the first integer: ")
        try:
            x = int(x)
            y = input("Please insert the second integer: ")
            try:
                y = int(y)
                print (haveProperty(x, y))
                running = False
            except:
                print("Error. The value was not an integer. Try again")
        except:
            print("Error. The value was not an integer. Try again")
    '''
    #version 2
    running = True
    while running:
        try:
            x, y = input("Please insert two integers: ").split()
            x = int(x)
            y = int(y)
            print (haveProperty(x, y))
            x = input()
            running = False
        except ValueError:
            print ("Error. You need to insert two integers. Try again")
        
