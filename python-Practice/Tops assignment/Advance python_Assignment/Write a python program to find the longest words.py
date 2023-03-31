#Write a python program to find the longest words
def largestWord(s):
	s = sorted(s, key = len)
	print(s[-1])
 
if __name__ == "__main__":
    s = "hello i am viraj makwana"
    l = list(s.split(" "))
    largestWord(l)
