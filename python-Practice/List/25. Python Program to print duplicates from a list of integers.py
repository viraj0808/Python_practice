# program to print duplicate numbers in a given list
# provided input
list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

new = [] # defining output list

# condition for reviewing every
# element of given input list
for a in list:

	# checking the occurrence of elements
	n = list.count(a)

	# if the occurrence is more than
	# one we add it to the output list
	if n > 1:

		if new.count(a) == 0: # condition to check

			new.append(a)

print(new)

