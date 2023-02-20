"""
    Case1. Average case. Inputs will be generated randomly.
    Case2. Worst case. Input will be a sorted list.
    InpType1. Each element of the list is an integer between 1 and 10*n. The elements are
              randomly chosen within this range. Note that the elements in the list will be
              mostly distant integers due to the interval used to choose the elements.
    InpType2. Each element of the list is an integer between 1 and 0.75*n. Note that in this case
              there will be duplicate elements in the list.
    InpType3. Each element of the list is an integer between 1 and 0.25*n. Note that in this case
              there will be much more duplicate elements in the list.
    InpType4. All the elements are the integer 1.
.                                                                                            """

import random
import sys
from quicksort_ver1 import mainv1                                    # tester.py calls main functions
from quicksort_ver2 import mainv2                                    # of different versions.
from quicksort_ver3 import mainv3
from quicksort_ver4 import mainv4


def testInputGenerator(Case, InpType, n):
    testInput = list()
    if   InpType == 1:
        testInput = [random.randint(1,10*n) for i in range(n)] 
    elif InpType == 2:
        testInput = [random.randint(1,0.75*n) for i in range(n)] 
    elif InpType == 3:
        testInput = [random.randint(1,0.25*n) for i in range(n)]         
    elif InpType == 4:
        testInput = [ 1 for i in range(n)]   

    if Case == 2:
        testInput.sort()
    return testInput

def printHypenized(L):
    print("[",end="")

    for i in range((len(L) - 1)):
        print(L[i], end="-")

    print(L[-1],end="]")
    print()
    
    return

def main():

    sys.setrecursionlimit(10000)

    Case    = 1                                         # HARDCODED SPECIFICATION I
    InpType = 2                                         # HARDCODED SPECIFICATION II
    n       = 100                                       # HARDCODED SPECIFICATION III
    print("Case:",Case,"InpType:",InpType,"n:",n)

    averageInputs = list()
    if Case == 1:
        for i in range(5):
            L = testInputGenerator(Case,InpType,n)
            print("INPUT average:",i+1)
            printHypenized(L)
            averageInputs.append(L)
    else:
        L = testInputGenerator(Case,InpType,n)
        print("INPUT worst:")
        printHypenized(L)
    
    average1=0
    average2=0
    average3=0
    average4=0
    if Case == 1:
        for i in range(5):
            duration = mainv1(averageInputs[i])
            average1+=duration

            duration = mainv2(averageInputs[i])
            average2+=duration

            duration = mainv3(averageInputs[i])
            average3+=duration

            duration = mainv4(averageInputs[i])
            average4+=duration

        print("average1:", (average1 / 5))
        print("average2:", (average2 / 5))
        print("average3:", (average3 / 5))
        print("average4:", (average4 / 5))


    elif Case == 2:
        duration = mainv1(L)
        print("mainv1:", duration)

        duration = mainv2(L)
        print("mainv2:", duration)

        duration = mainv3(L)
        print("mainv3:", duration)

        duration = mainv4(L)
        print("mainv4:", duration)        

    return

if __name__ == "__main__":
    main()