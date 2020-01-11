def printStack(stack, seq):
    for i in range(len(stack)):
        print (str(seq[stack[i]]) + " ", end = "")
    print ()

def recBKT(n, pos, stack, seq):
    if pos >= n:
        return
    
    printStack(stack, seq)
    
    for i in range(pos, n):
        if seq[i] > seq[stack[-1]]:
            stack.append(i)
            recBKT(n, i + 1, stack, seq)
            
    temp = stack.pop()
    #we have finished all the sequences which begin with a particular value, so we continue with all the sequences
    #which start with the next value in the sequence
    if len(stack) == 0:
        stack.append(temp + 1)
        recBKT(n, temp + 1, stack, seq)
            
def BKT(n, stack, seq):
    stack.append(0)
    printStack(stack, seq)
    i = -1
    
    while(len(stack) > 0):
        top = stack[-1]
        if i == -1:
            i = top + 1
        
        while i < n:
            if seq[i] > seq[top]:
                stack.append(i)
                printStack(stack, seq)
                i = n + 1
            i += 1
        
        #the while loop has not found any new elements (we haven't reached the 'i = n + 1' line)
        #which means that the current top of the stack does not have any successors larger than it
        #when this happens, we need to continue the search of the previous top, which requires us to set the index
        #to the position it had before the new top was added, which is exactly the position after the top
        if i == n:
            i = stack.pop() + 1
            
            #we have finished all the sequences which begin with a particular value, so we continue with all the sequences
            #which start with the next value in the sequence
            if len(stack) == 0 and i < n:
                stack.append(i)
                print (seq[i])
        else:
            i = -1

def main():
    sequence = [2, 1, 3, 5, 4, 0]
    
    stack = [0, ]

    recBKT(len(sequence), 0, stack, sequence)
    print ("\n\n\n")
    
    stack = []
    BKT(len(sequence), stack, sequence)
    
    
if __name__ == "__main__":
    main()