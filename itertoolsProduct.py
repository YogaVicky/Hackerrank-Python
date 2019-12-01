from itertools import product
s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))
s3 = list(product(s1,s2))
for i in range(len(s3)):
	print(s3[i],end=" ")
