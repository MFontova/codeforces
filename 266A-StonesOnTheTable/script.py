import sys
sys.stdin = open("input.txt")

n = int(input())

stones = input()

counter = 0
for i in range(len(stones[0:-1])):
    current_stone = stones[i]
    next_stone = stones[i + 1]

    if(current_stone == next_stone):
        counter += 1

print(counter)