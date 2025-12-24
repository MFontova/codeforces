import sys
sys.stdin = open('input.txt')

n = input()

planes = [int(p) for p in input().split(' ')]

print(planes)

graph = {}

for plane in planes:
  graph[plane] = planes[plane - 1]

print(graph)

currentPosition = planes[0]

stack = [graph[currentPosition]]

for pair in graph:
  print('pair', pair)

# visited = set()

# while len(stack) > 0:
#   visited.add(currentPosition)
#   print('stack', stack)
#   currentPosition = stack.pop()
#   if currentPosition not in visited:
#     stack.append(graph[currentPosition])

# if len(visited) == 3:
#   print('YES')
# else:
#   print('NO')