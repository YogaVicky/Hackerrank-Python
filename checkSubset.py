ch = int(input())
for i in range(ch):
	n = int(input())
	s1 = set(map(int,input().split()))
	m = int(input())
	s2 = set(map(int,input().split()))
	if len(s1.intersection(s2)) == len(s1):
		print("True")
	else:
		print("False")
