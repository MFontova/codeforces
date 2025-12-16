import sys
sys.stdin = open('input.txt')

n = input()

print(n)

current = '0'
counter = 0

for i in n:
    if i == current:
        counter += 1
    else:
        current = i
        counter = 0