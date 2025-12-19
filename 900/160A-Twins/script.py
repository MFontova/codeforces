import sys

sys.stdin = open('input.txt')

n = int(input())

coins = [int(coin) for coin in input().split(' ')]

coins.sort(reverse=True)

for i in range(n):
    me = coins[0 : i+1]
    twin = coins[i+1:]

    print('me', me)
    print('twin', twin)

    if(sum(me) > sum(twin)):
        print(len(me))
        break