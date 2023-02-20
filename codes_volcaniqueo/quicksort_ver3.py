
"""
    This python program is the basic implementation of
    Randomized Algorithm 2: 
        The list is first randomly permuted and then the classical
        deterministic algorithm is called where the pivot is chosen as the first element of the list. 
        This is the algorithm “Quicksort (2nd version)” in the course slides.
.                                                                                    """
import random
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

def mainv3(L):
    
    begin = time.time()

    for i in range(len(L)-1):               #Shuffle the input array.
        rand = random.randint(0,len(L)-1)
        listElementAtIndex_i = L[i]
        listElementAtIndex_j = L[rand]
        L[i] = listElementAtIndex_j
        L[rand] = listElementAtIndex_i

    result = QuickSort(L)
    end = time.time()

    return (end-begin)

