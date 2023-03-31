#Write a Python program to read last n lines of a file.

def LastNlines(fname, N):
	
	with open(fname) as myfile:
		
		
		for line in (myfile.readlines() [-N:]):
			print(line, end ='')


if __name__ == '__main__':
	fname = 'myfile.txt'
	N = 2
	try:
		LastNlines(fname, N)
	except:
		print('File not found')
