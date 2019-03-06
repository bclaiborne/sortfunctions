tree = [1,5,7,4,6,9,13,3]

#sort the tree
#compare index value to index+1
for i in range(1, len(tree)): 
	j = i - 1
	value = tree[i]

	while (value < tree[j]):
		print(str(value)+ " < " +str(tree[j]))
		j -= 1
		if value < tree[j]:
			tree.insert(j, value)
		else:
			tree.insert(i, value)
	print("i= "+str(i)+" ,j= "+str(j)+" value= "+str(value))
	
		
	print(tree)
		
		
#if i+1 > i do nothing
#if i > i+1 remove n+1 from the list and add it before n

