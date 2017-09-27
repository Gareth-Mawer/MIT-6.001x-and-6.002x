"""
Midterm Exam Programming Questions from MIT 6.00.1x Course
Author: Gareth Mawer
"""

# Problem 4, previous problems were multiple choice questions
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    def isSmaller(a, b):
        if abs(a) <= b:
            return a
        else:
            return b
    exponent1 = 0
    exponent2 = 1
    while base**exponent1 <= num:
        if base**exponent2 >num and base**exponent1 - num == isSmaller(base**exponent1 - num, base**exponent2 - num):
            return exponent1
        elif base**exponent2 >num and base**exponent2 - num == isSmaller(base**exponent1 - num, base**exponent2 - num):
            return exponent2
        else:
            exponent1 += 1
            exponent2 += 1

# Problem 5
def dotProduct(listA, listB):
    """
    listA: a list of numbers
    listB: a list of numbers of the same length as listB
    
    Returns the dot product of all the numbers in the lists.
    """
    dotProd = 0
    for num in range(len(listA)):
        prod = listA[num] * listB[num]
        dotProd = dotProd + prod
    return dotProd


# Problem 6
# If L = [[1, 2], [3, 4], [5, 6, 7]], then deep_reverse(L) gives [[7, 6, 5], [4, 3], [2, 1]]
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    L.reverse()
    for i in L:
        if type(i) == list:
            deep_reverse(i)

# Problem 7 - Must mutate list

# Example 1
# If f(a, b) returns a + b, d1 = {1:30, 2:20, 3:30, 5:80}, d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})

# Example 2
# If f(a, b) returns a > b, d1 = {1:30, 2:20, 3:30}, d2 = {1:40, 2:50, 3:60}
# then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    tupDict = []
    tupDict1 = []
    for i in d1.keys():
        if i in d2.keys():
            tupDict.append((i, (f(d1[i], d2[i]))))
        elif i not in d2.keys():
            tupDict1.append((i, d1[i]))
        for i in d2.keys():
            if i not in d1.keys():
                tupDict1.append((i, d2[i]))
    return (dict(tupDict), dict(tupDict1))

# Problem 8

# =================================
# Example
# def f(i):
#    return i + 2
# def g(i):
#    return i > 5

# L = [0, -10, 5, 6, -4]
# print(applyF_filterG(L, f, g))  --> 6
# print(L) --> [5, 6]
# =================================

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    def test(l):
        if len(l) == 0:
            return True
    l = L[:]
    for i in l:
        f(i)
        if not g(f(i)):
            L.remove(i)
    if test(L):
        return -1
    else:
        return max(L)

# Problem 9
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    H = aList[:]
    L = []
    j = 0
    for i in range(len(H)):
        if type(H[i]) == list:
            j += i + abs((len(L) - len(H)))
            L = L + flatten(H[i])
        else:
            j += 1
            L.insert(j, H[i])
    aList = L
    return aList

# Attempt 2 at Problem 9
def flatten1(l):
    L = []
    for element in l:
        if type(element) == list:
            L = L + flatten1(element)
        else:
            L.append(element)
    return L





