import sys
sys.stdin = open("input.txt")

[limark, bob] = [int(n) for n in input().split(' ')]

years = 0
while limark <= bob :
	limark = limark * 3
	bob = bob * 2
	years += 1

print(years)