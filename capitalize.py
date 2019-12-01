# Complete the solve function below.
def solve(s):
    s = list(s.split(" "))
    f = s[0].capitalize()
    for i in range(1,len(s)):
        s[i] = s[i].capitalize()
        f = f + " " + s[i]
    return f

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

