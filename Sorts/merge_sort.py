def merge(s1, s2):
    '''
    A merge function which merges two sorted lists using two moving pointers. Stable.
    '''
    i = j = 0
    merged = []
    for _ in range(len(s1) + len(s2)):
        if i < len(s1):
            if j < len(s2):
                if s1[i] <= s2[j]:
                    merged.append(s1[i])
                    i += 1
                else:
                    merged.append(s2[j])
                    j += 1
            else:
                merged.append(s1[i])
                i += 1

        else:
            if j < len(s2):
                merged.append(s2[j])
                j += 1
    return merged


def merge_sort(s):
    '''
    Recursively sorts a list by splitting into two sublists, sorting those, and merging.
    Base-case: if the list only contains one element, return the same list.
    '''

    if len(s) == 1:
        return s

    left = merge_sort(s[:len(s)//2])
    right = merge_sort(s[len(s)//2:])

    return merge(left, right)