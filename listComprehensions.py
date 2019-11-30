x = int(input())
y = int(input())
z = int(input())
n = int(input())
mainlist = []
for i in range(x+1):
	for j in range(y+1):
		for k in range(z+1):
			if (i + j + k)!=n:
				sublist = [i,j,k]
				mainlist.append(sublist)
print(mainlist)
