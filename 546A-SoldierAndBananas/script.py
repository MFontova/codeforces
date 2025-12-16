import sys
sys.stdin = open("input.txt")

[first_banana, dollars, wanted_bananas] = [int(n) for n in input().split(' ')]

cost = 0
for i in range(wanted_bananas):
    cost += (i + 1) * first_banana

if(cost - dollars > 0):
    print(cost - dollars)
else:
    print(0)