import sys
sys.stdin = open("input.txt")

import math

n = input().split(' ')

[x, y] = [int(num) for num in n]

print(math.trunc(x*y/2))