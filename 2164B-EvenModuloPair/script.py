import sys
sys.stdin = open("input.txt")

n = int(input())

for line in range(n):
  length = int(input())
  sequence = [int(num) for num in input().split(' ')]

  combination = []
  for i in range(length - 1):
    if(len(combination) > 0):
      break
    for j in range(i + 1, length):
      modulo = sequence[j] % sequence[i]

      if(modulo % 2 == 0):
        if(len(combination) == 0):
          combination = [sequence[i], sequence[j]]
          break

  if(len(combination) == 0):
    print(-1)
  else:
    print(combination[0], combination[1])
