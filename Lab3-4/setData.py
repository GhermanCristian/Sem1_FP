from validators import isValidNumber

#setter
def setStudentGrades(P1, P2, P3):
    return (P1, P2, P3)

def createStudent(P1, P2, P3):
    '''
    Creates a student with the grades P1, P2, P3, if the data is valid
    @param:
        - P1, P2, P3 - grades of a student
    @return: 
        - a tuple of the form (P1, P2, P3), if the data is valid
        - -1, otherwise
    '''
    P1 = isValidNumber(P1, 'I')
    P2 = isValidNumber(P2, 'I')
    P3 = isValidNumber(P3, 'I')
    
    if P1 != -1 and P2 != -1 and P3 != -1:
        return setStudentGrades(P1, P2, P3)
    
    return -1