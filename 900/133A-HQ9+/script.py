import sys
sys.stdin = open('input.txt')

instructions = list(input())

filtered = list(filter(lambda x: x in ['H', 'Q', '9'], instructions))

if(len(list(filtered)) == 0):
  print('NO')
else:
  print('YES')