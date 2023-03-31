#Write a Python program to copy the contents of a file to another file.
# open both files
with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile:
	for line in firstfile:
			secondfile.write(line)

