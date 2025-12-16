import sys
sys.stdin = open("input.txt")

[n ,k] = [int(inp) for inp in input().split(' ')]

res = n

for i in range(k):
    if(res % 10 == 0):
        res = res/10
    else:
        res -= 1

print(int(res))