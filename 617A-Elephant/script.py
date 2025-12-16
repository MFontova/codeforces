import sys
sys.stdin = open("input.txt")

origin = 0
destiny = int(input())

moves = [1,2,3,4,5]

steps = 0

while origin < destiny:
    for move in reversed(moves):
        if(move <= destiny - origin):
            origin += move
            steps += 1
            break

print(steps)