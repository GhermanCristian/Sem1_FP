#lab 1 - set 3 - ex 15
'''
Generate the largest perfect number smallerthan a given natural number n. If such a number does not exist, a message should be displayed. A number is perfect if it is equal to the sum of its divisors, except itself.
(e.g. 6 is a perfect number, as 6=1+2+3).
'''

#gets the sum of the divisors of x
def getDivisorSum(x):
    divSum = 1
    for div in range(2, x):
        if x % div == 0:
            divSum += div
    return divSum

#determines if integer x is a perfect number; returns a boolean value
def isPerfect(x):
    return x == getDivisorSum(x)

#gets the largest perfect value smaller than 'n'; returns an integer if a result is found, else returns None
def getLargestPerfect(n):
    while n > 2:
        n -= 1
        if isPerfect(n):
            return n
        
    #no perfect number has been found
    return None

def main():
    while True:
        x = input("Please insert an integer: ")
        try:
            x = int(x)
            x = getLargestPerfect(x)

            #a result has not been found
            if x == None:
                print ("There are no such numbers")
            else:
                print ("The result is: %d" % (x))

            break

        #x was not an integer, try again
        except:
            print ("This is not an integer")
            
if __name__ == "__main__":
    main()
