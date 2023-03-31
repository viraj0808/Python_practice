#Write a Python program to read a file line by line and store it into a list
with open('myfile.txt') as f:
    lines = [line.rstrip() for line in f]
  
print(lines)