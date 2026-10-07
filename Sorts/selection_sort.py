def selection_sort(s):
    '''
    Sorts a list by swapping the kth element with min(s[k+1:]) at the kth step. Needs len(s) - 1 steps in total.
    Unstable; in place.
    Best and worst case: O(n^2) time complexity.
    Returns (sorted_list, comparisons, swaps)
    '''
    comparisons = 0
    swaps = 0

    for k in range(len(s) - 1):
        smallest = k
        for j in range(k+1, len(s)):
            if s[j] < s[smallest]:
                comparisons += 1
                smallest = j # Update smallest index
        if smallest != k: # if there is no element smaller than s[k] in the remaining list, don't swap.
            swaps += 1
            s[k], s[smallest] = s[smallest], s[k]

    return (s, comparisons, swaps)

