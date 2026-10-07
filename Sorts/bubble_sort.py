def bubble_sort(s):
    '''
    Sorts a list by swapping adjacent elements if they are in the wrong order.
    At the end of k passes, the largest k elements are sorted at the top of the list. Takes len(s)-1 passes.
    Stable; in place, non adaptive.
    Best case: 0 swaps, O(n^2) comparisons
    Worst case: O(n^2) swaps and O(n^2) comparisons
    Returns (sorted_list, comparisons, swaps)
    '''
    comparisons = 0
    swaps = 0
    for k in range(len(s) - 1, 0, -1):
        for j in range(k):
            comparisons += 1
            if s[j] > s[j+1]:
                swaps += 1
                s[j], s[j+1] = s[j+1], s[j]

    return (s, swaps, comparisons)


def bubble_sort_optimized(s):
    '''
    Same as above, but breaks out when there are no comparisons made during a complete pass.

    Stable; in place, adaptive.

    Best: 0 swaps, n-1 comparisons
    Worst: O(n^2) swaps, O(n^2) comparisons (no change from normal bubble sort)
    '''
    comparisons = 0
    swaps = 0

    for k in range(len(s) - 1, 0, -1):
        topass = False
        for j in range(k):
            comparisons += 1
            if s[j] > s[j+1]:
                topass = True
                swaps += 1
                s[j], s[j+1] = s[j+1], s[j]
        if not topass:
            break
    return (s, swaps, comparisons)




