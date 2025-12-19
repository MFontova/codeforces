import sys
sys.stdin = open('input.txt')

[n, m, a] = [int(x) for x in input().split(' ')]

vertical = 0
horizontal = 0

if(n >= a):
  vertical = n - a

if(m >= a):
  horizontal = m - a

print(horizontal + vertical)