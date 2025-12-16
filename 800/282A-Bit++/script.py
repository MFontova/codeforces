import sys
sys.stdin = open("input.txt")

n = int(input())

result = 0
for i in range(n):
  line = input()
  if ('++' in line):
    result += 1
  if ('--' in line):
    result -= 1

print(result)