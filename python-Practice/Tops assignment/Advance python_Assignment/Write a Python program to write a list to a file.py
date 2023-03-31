#Write a Python program to write a list to a file.
l = ['makwana','viraj','makwana']

with open('myfile.txt', 'w+') as f:
	for items in l:
		f.write('%s\n' %items)
	print("File written successfully")
f.close()
