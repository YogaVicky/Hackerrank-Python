n = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
subset = alpha[:n]
base = "-".join(reversed(subset))
# print(base)
rows = []
# e-d-c-b-a
for i in range(n):
	row = base[:len(base) - i*2]
	row = ("-" * (len(base) - len(row))) + row
	print(row)
	row1 = row[:-1]
	print(row1)
	row1 = "".join(reversed(row1))
	print(row1)
	row = row + row1
	rows.insert(0, row)
for i in range(2,n+1):
	rows.append(rows[n-i])
for i in range((n-1)*2+1):
	print(rows[i])