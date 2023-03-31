#Write a Python program to read first n lines of a file.
f = open("myfile.txt","r")
for i in range(f):
	print(f.readline())