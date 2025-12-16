import sys
sys.stdin = open("input.txt")

n = input()

lucky_numbers = ['4', '7']

counter = 0
for i in n:
    if i in lucky_numbers:
        counter += 1

if str(counter) in lucky_numbers:
    print('YES')
else:
    print('NO')