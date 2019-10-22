#lab 1 - set 2 - ex 10
'''
The  palindrome  of  a  number  is  the  number  obtained  by  reversing  the  order  of its digits(e.g. the palindrome of 237is 732).
For a given natural number n, determine its palindrome.
'''

#returns the palindrome of x (integer)
def getPalindrome(x):
    pal = 0
    while x > 0:
        pal = pal * 10 + x % 10
        x = x // 10

    return pal

def main():
    while True:
        x = input("Please insert an integer: ")
        try:
            x = int(x)
            print (getPalindrome(x))
            break
        except:
            print ("This is not an integer.")

if __name__ == "__main__":
    main()
