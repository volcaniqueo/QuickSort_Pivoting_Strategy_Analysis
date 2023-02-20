
"""
    This python program is the basic implementation of
    Classical Deterministic Algorithm.
    
    Implementation complies with the QuickSort pseudo-code from the course slides.

.                                                                                    """

import time

def QuickSort(L):
    
    if(len(L) > 1):
        position   = Rearrange(L)
        leftArray  = QuickSort(L[:(position)]  )
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

def mainv1(L):
    begin = time.time()
    result = QuickSort(L)
    end = time.time()

    return (end-begin)




