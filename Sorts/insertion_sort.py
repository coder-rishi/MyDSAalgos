def insertion_sort(s):
    '''
    Sorts a list by swapping the (k+1)th element repeatedly with its previous elements till it reaches an appropriate position.
    Stable; 
    '''
    n = len(s)
    for k in range(0, n-1):
        for j in range(k+1, 0, -1):
            if s[j]<s[j-1]:
                s[j], s[j-1] = s[j-1], s[j]
            else:
                break
    return s

print(insertion_sort([5, 4, 3, 2, 1, 100]))