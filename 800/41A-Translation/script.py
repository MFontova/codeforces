import sys
sys.stdin = open("input.txt")

a = input()
b = input()

if a == b[::-1]:
    print('YES')
else:
    print('NO')