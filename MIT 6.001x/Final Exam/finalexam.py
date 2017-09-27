"""
Final Exam Programming Questions from MIT 6.00.1x Course
Author: Gareth Mawer
"""

#Problem 3
# Numbers in Mandarin follow 3 simple rules:
#    1. There are words for each of the digits from 0 to 10.
#    2. For numbers 11-19, the number is pronounced as "ten digit", so for example, 16 would be pronounced (using Mandarin) as "ten six".
#    3. For numbers between 20 and 99, the number is pronounced as “digit ten digit”, so for example, 37 would be pronounced (using Mandarin) as "three ten seven". If the digit is a zero, it is not included. 

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # ============================================================================
    # Nested Function
    def mandarinConversion(us_num):
        '''
        us_num, a string representing a US number 0 to 99
        returns the string mandarin represntation of us_num
        '''
        if us_num[-1] == '0':
            return trans[us_num[0]] + ' ' + trans['10']
        elif us_num[-1] != '0':
            return trans[us_num[0]] + ' ' + trans['10'] + ' ' + trans[us_num[-1]]
    # ============================================================================
    # convert_to_mandarin body
    if int(us_num) <= 10:
        return trans[us_num]
    elif int(us_num) >= 11 and int(us_num) < 20:
        return trans['10'] + ' ' + trans[us_num[-1]]
    elif int(us_num) >= 20 and int(us_num) < 100:
        return mandarinConversion(us_num)

# Problem 4

# Definitions:
# Monotonically increasing means that a number at position k+1 in A sequence is greater than or equal to the number at position k in the same sequence.
# Monotonically decreasing means that a number at position k+1 in A sequence is less than or equal to the number at position k in the same sequence.

# Example
# If L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] then the longest run of monotonically increasing numbers in L is [3, 4, 5, 7, 7] and the 
# longest run of monotonically decreasing numbers in L is [10, 4, 3]. Your function should return the value 26 because the 
# longest run of monotonically increasing integers is longer than the longest run of monotonically decreasing numbers. 


def longest_run(L):
    '''
    L,a list with length greater than two
    returns the sum of all the elements of the longest monotonic list within L
    '''
    # ============================================================================
    # Nested Function
    def largestList(L1, L2, L3):
        '''
        L1, L2, are lists with alength greater than two. 
        returns the largest list
        '''
        if len(L1) > len(L3) and len(L1)>=len(L2):
            return L1
        elif len(L2) > len(L3) and len(L2)>=len(L1):
            return L2
        else:
            return L3
    # ============================================================================
    # longest_run body
    longestList = []    
    longestListSum = 0
    for i in range(len(L)):
        h = i
        monotonicInc = []
        monotonicDec = []
        monotonicInc.append(L[h])
        for j in range(i+1,len(L)):
            if L[j] >= L[h]:
                monotonicInc.append(L[j])
                h += 1
            else:
                break
        h = i
        monotonicDec.append(L[h])
        for j in range(i+1,len(L)): 
            if L[h] >= L[j]:
                monotonicDec.append(L[j])
                h += 1
            else:
                break
        longestList = largestList(monotonicInc, monotonicDec, longestList)
    for number in longestList:
        longestListSum += number
    return longestListSum

# Problem 5
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        if status == 'citizen' or status == 'legal_resident' or status == 'illegal_resident':
            self.status = status
        else:
            raise ValueError
        
    def getStatus(self):
        """
        Returns the status
        """
        return self.status

# Problem 6
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return Professor.say(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff

# Problem 7
def general_poly(L):
    """ 
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """
    def poly(L, base):
        '''
        
        '''
        polySum = 0
        exponent = len(L)-1
        for number in L:
            polySum += number*base**exponent
            exponent -= 1
        return polySum
    def polyF(x, l = L):
        return poly(l, x)
    return polyF

