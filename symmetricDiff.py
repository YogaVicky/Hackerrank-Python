n = int(input())
s1 = set(map(int,input().split()))
m = int(input())
s2 = set(map(int,input().split()))
res = list((s1.union(s2)).difference(s1.intersection(s2)))
res.sort()
for i in range(len(res)):
	print(res[i])