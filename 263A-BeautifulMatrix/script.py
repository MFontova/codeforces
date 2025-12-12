import sys
sys.stdin = open("input.txt")

matrix = []
for i in range(5):
  matrix.append(input().split(' '))

count = 0
for i in range(len(matrix)):
  line = matrix[i]
  if('1' in line):
    index = line.index('1')
    count += abs(2 - i)
    count += abs(2 - index)

print(count)