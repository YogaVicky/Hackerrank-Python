def merge_the_tools(string, k):
	t = len(string)//k
	f = 0
	for i in range(t):
		s = []
		for j in range(k):
			s.append(string[f])
			f = f+1
		s = list(dict.fromkeys(s))
		s1 = "".join(s)
		print(s1)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)