n = int(input())
mainlist = []
choicelist = []
for i in range(n):
	ch = input()
	choicelist.append(ch)
for i in range(n):
	ch = list(choicelist[i].split())
	if ch[0] == "insert":
		mainlist.insert(int(ch[1]) , int(ch[2]))
	elif ch[0] == "remove":
		mainlist.remove(int(ch[1]))
	elif ch[0] == "print":
		print(mainlist)
	elif ch[0] == "append":
		mainlist.append(int(ch[1]))
	elif ch[0] == "sort":
		mainlist.sort()
	elif ch[0] == "reverse":
		mainlist.reverse()
	else:
		mainlist.pop()
