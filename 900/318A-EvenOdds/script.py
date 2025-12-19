import sys
sys.stdin = open('input.txt')

import math
[max, position] = [ int(n) for n in input().split(' ') ]

center = math.ceil(max / 2)

if(position <= center):
  print(position * 2 - 1)
else:
  print((position - center) * 2)