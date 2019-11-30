n = int(input())
scores = list(map(int,input().strip().split()))[:n]
scores.sort(reverse = True)
max = scores[0]
for i in range(n):
    if scores[i] < max:
        print(scores[i])
        break