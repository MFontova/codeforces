import sys
sys.stdin = open("input.txt")

n = int(input())

games = input()

a = 0
for i in range(n):
    if games[i] == 'A':
        a += 1

if a > n/2:
    print('Anton')

if a < n/2:
    print('Danik')

if a == n/2:
    print('Friendship')