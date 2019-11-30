def count_substring(string, sub_string):
	check = 0
	for i in range(0,len(string) - len(sub_string) + 1):
		sub = ""
		for j in range(i,i + len(sub_string)):
			sub = sub + string[j]
		if sub == sub_string:
			check = check + 1
	return check

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)