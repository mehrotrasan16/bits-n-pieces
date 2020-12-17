# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

# Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

# Example

    # For sequence = [1, 3, 2, 1], the output should be
    # almostIncreasingSequence(sequence) = false.

    # There is no one element in this array that can be removed in order to get a strictly increasing sequence.

    # For sequence = [1, 3, 2], the output should be
    # almostIncreasingSequence(sequence) = true.

    # You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

# Input/Output

    # [execution time limit] 4 seconds (py3)

    # [input] array.integer sequence

    # Guaranteed constraints:
    # 2 ≤ sequence.length ≤ 105,
    # -105 ≤ sequence[i] ≤ 105.

    # [output] boolean

    # Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.

import copy
from collections import Counter

def find_bad_pair(sequence):
    for i in range(0,len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1


def almostIncreasingSequence(sequence):
    j = find_bad_pair(sequence)
    if j == -1:
        return True
    if find_bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True
    if find_bad_pair(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True
    return False
# Sol # 2
    # for n,i in enumerate(sequence):
    #     lis = sequence.copy()
    #     del(lis[n])
    #     if len(lis) == len(set(lis)): 
    #         if sorted(lis) == lis :
    #             return True

    # return False
# Sol # 1 
    # flag = True
    # c = Counter(sequence)
    
    # for i in c.values():
    #     if i > 1:
    #         return False
    
    # for item in sequence:
    #     cleanseq = copy.copy(sequence)
    #     cleanseq.remove(item) 
    #     print(cleanseq)
    #     if len(cleanseq) == len(set(cleanseq)):
    #         if cleanseq == sorted(cleanseq):
    #             return True
            
    
    # return False
