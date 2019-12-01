ch = list(map(int , input().split()))
mainlist = []
for i in range(ch[1]):
	ch1 = list(map(float , input().split()))
	mainlist.append(ch1)
for i in range(ch[0]):
	res = 0
	for j in range(ch[1]):
		res = res + mainlist[j][i]
	res = res/ch[1]
	print(res)