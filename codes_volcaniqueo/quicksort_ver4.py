
"""
    This python program is the basic implementation of
    The deterministic algorithm:
        The pivot is chosen according to the “median of three” rule.
.                                                                                    """

import time

def QuickSort(L):
    if(len(L) > 1):
        position = Rearrange(L)
        leftArray =  QuickSort(L[:(position)]  )
        rightArray = QuickSort(L[(position+1):])
        return leftArray + [L[position]] + rightArray
    return L

def Rearrange(L):
    right = 0                                 #low
    left  = len(L)                            #high + 1

    median = findMedianOfThree(L)
    temp = L[median]
    L[median] = L[0]
    L[0] = temp
    x = L[0]
    while right < left:
        right += 1
        left  -= 1
                    
        while L[right] < x: #repeat until L[right] >= x
            right += 1
            if right >= len(L):
                break

        while L[left ] > x: #repeat until L[left ] <= x
            left  -= 1 
            if left <= -1:
                break

        if right < left:
            listElementAtIndex_i = L[right]
            listElementAtIndex_j = L[left]
            L[right] = listElementAtIndex_j
            L[left] = listElementAtIndex_i
            
    position = left
    L[0] = L[position]
    L[position] = x
    return position

def findMedianOfThree(L):               #Finds the median element of the list.
    lowIndex = 0                            #Returns the index of the element.
    highIndex = len(L)-1
    middleIndex = ( (len(L)-1) // 2)

    low = L[lowIndex]
    high = L[highIndex]
    middle = L[middleIndex]

    trio = [low,high,middle]
    trio.sort()

    if trio[1] == low:
        return lowIndex
    elif trio[1] == high:
        return highIndex
    else:
        return middleIndex

def mainv4(L):
    begin = time.time()
    result = QuickSort(L)
    end = time.time()

    return (end-begin)
