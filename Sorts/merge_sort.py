# Merge: s1, s2 -> s
def merge(s1, s2):
	 i = j = 0 # A two pointer implementation
	 merged = []
	 for _ in range(len(s1) + len(s2)):
		if i < len(s1):
			if j <len(s2):
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


# Merge Sort: s -> s
def merge_sort(s):
	 if len(s) == 1:
		return s

	s1 = merge_sort(s[:len(s)//2])
	s2 = merge_sort(s[len(s)//2:])
	# Recursive
	return merge(s1, s2)