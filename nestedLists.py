n = int(input())
mainlist = []
sortlist = []
for i in range(n):
	sublist = []
	sublist.append(input())
	sublist.append(float(input()))
	mainlist.append(sublist)
for i in range(n):
	for j in range(i,n):
		if mainlist[i][1] > mainlist[j][1]:
			temp =  mainlist[i]
			mainlist[i] = mainlist[j]
			mainlist[j] = temp
min = mainlist[0][1]
for i in range(1,n):
	if mainlist[i][1] > min:
		min = mainlist[i][1]
		break
for i in range(0,n):
	if mainlist[i][1] == min:
		sortlist.append(mainlist[i])
for i in range(len(sortlist)):
	for j in range(i+1 , len(sortlist)):
		if sortlist[i][0] > sortlist[j][0]:
			temp = sortlist[i]
			sortlist[i] = sortlist[j]
			sortlist[j] = temp
for i in range(len(sortlist)):
	print(sortlist[i][0])
