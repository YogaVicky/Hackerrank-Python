n = int(input())
mainlist = []
for i in range(n):
	sublist = list(input().split())
	for j in range(1,4):
		sublist[j] = float(sublist[j]);
	mainlist.append(sublist)
check = input()
for i in range(n):
	if check == mainlist[i][0]:
		break
avg = float((mainlist[i][1] + mainlist[i][2] + mainlist[i][3]) / 3)
avg = round(avg,2)
print('%.2f' % avg)

