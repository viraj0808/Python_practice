# Python program to sort values of first list based on second list
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
a = list(set(list2))
a.sort()
res = []
for i in a:
	for j in range(0, len(list2)):
		if(list2[j] == i):
			res.append(list1[j])
print(res)
