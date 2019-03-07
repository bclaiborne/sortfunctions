tree = [1,5,7,4,6,9,13,3]

#sort the tree
#compare index value to index-1
for j in range(1, len(tree)): 
	i = j - 1
	value = tree[j]
	
	#compare value with the index just below and dont wrap
	while (value < tree[i] and i > -1):
		#if value is less than the value in the comparison slot move the compare slot to the value's original slot
		tree[i+1] = tree[i]
		#then move left to compare again
		i = i-1
	#once we have moved down i slots and the i slot value isn't > our value, write the value into the slot to the right.
	tree[i+1] = value
		
print(tree)