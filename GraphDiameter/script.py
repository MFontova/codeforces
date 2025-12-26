import sys
sys.stdin = open("input.txt")

n = int(input())

# Graph generation
graph = {}
for i in range(n):
  [k, v] = [node for node in input().split(' ')]
  if k in graph.keys():
    graph[k].append(v)
  else:
    graph[k] = [v]

print(graph)

# create a register dictionary with structure {key: [weight, path]}
register = {}

# BFS and fill register
start = list(graph.keys())[0]
queue = [[start, 0, [start]]]

while len(queue) > 0:
  [currentNode, weight, path] = queue.pop(0)
  register[currentNode] = [weight, path]

  if currentNode in graph.keys():
    children = graph[currentNode]
    for child in children:
      queue.append([child, weight + 1, [*path, child]])

# Found largest key
largestKey = ''
largest = 0
for key in register.keys():
  if(register[key][0] > largest):
    largest = register[key][0]
    largestKey = key

# From largest key, calculate diameter
# Necessari refactoritzar perque ara esta comparant amb tots els nodes i nomes ho hauria de fer amb les fulles
diameter = 0
[firstValue, firstPath] = register[largestKey]
for key in register.keys():
  [secondValue, secondPath] = register[key]

  lastCommon = None
  for a, b in zip(firstPath, secondPath):
    if a == b:
      lastCommon = a
    else:
      break

  lastCommonValue = register[lastCommon][0]

  newDiameter = firstValue - lastCommonValue + secondValue - lastCommonValue

  diameter = max(diameter, newDiameter)

print('diameter', diameter)