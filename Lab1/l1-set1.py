#lab 1 - set 1 - ex 5
'''
Generate  the  largest prime  number  smaller  than  a  given  natural  number n.
If  such  anumber does not exist, a message should be displayed.
'''

#checks if integer 'x' is prime; returns a boolean value
def isPrime(x):
    if x == 0 or x == 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

#gets the largest prime value smaller than 'n'; returns an integer if a result is found, else returns None
def getLargestPrime(n):
    while n > 2:
        n -= 1
        if isPrime(n):
            return n
        
    #no prime number has been found
    return None

def main():
    while True:
        x = input("Please insert an integer: ")
        try:
            x = int(x)
            x = getLargestPrime(x)

            #a result has been found
            if not x == None:
                print ("The result is: %d" % (x))
            else:
                print ("There are no such numbers")
            break

        #x was not an integer, try again
        except:
            print ("This is not an integer")
            
if __name__ == "__main__":
    main()
