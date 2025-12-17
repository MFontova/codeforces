import sys
sys.stdin = open('input.txt')

n = input()

current = '0'
counter = 0

for i in n:
    if i == current:
        counter += 1
    else:
        current = i
        counter = 1

    if counter == 7:
        break

if counter == 7:
    print('YES')

else:
    print('NO')
