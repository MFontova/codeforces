import sys
sys.stdin = open('input.txt')

n = input()

planes = [int(p) for p in input().split(' ')]

graph = {}
pairsList = []

for plane in planes:
  graph[plane] = planes[plane - 1]
  pairsList.append([plane, planes[plane - 1]])

groups: list[set[int]] = []

for [a,b] in pairsList:
  print(a,b)
  
  if len(groups) == 0:
    groups.append(set([a,b]))
  for i in range(len(groups)):
    group = groups[i]
    if(a in group or b in group):
      groups[i].add(a)
      groups[i].add(b)
      break
    
  groups.append(set([a,b]))

  print(groups)


print(groups)

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