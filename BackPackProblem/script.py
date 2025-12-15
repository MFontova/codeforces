import sys
sys.stdin = open("input.txt")

w = int(input())

n = int(input())

weights = [0]
values = [0]
names = ['_']
for i in range(n):
  [object_name, object_weight, object_value] = [o for o in input().split(' ')]
  names.append(object_name)
  weights.append(int(object_weight))
  values.append(int(object_value))

dp = [[0 for i in range(w + 1)] for i in range(n + 1)]

for i in range(1, len(dp)):
  o_weight = weights[i]
  o_value = values[i]
  for j in range(len(dp[i])):
    current_capacity = j
    if(o_weight > current_capacity):
      dp[i][j] = dp[i - 1][j]
    else:
      value_no_including = dp[i - 1][j]

      capacity_rest = current_capacity - o_weight

      value_including = o_value + dp[i - 1][capacity_rest]

      dp[i][j] = max(value_no_including, value_including)



selected_objects = []
curr_capacity = w
i = n

while(i > 0 and curr_capacity > 0):
  if(dp[i][curr_capacity] != dp[i - 1][curr_capacity]):
    selected_objects.append(names[i])
    added_weight = weights[i]
    curr_capacity -= added_weight

  i -= 1

print(selected_objects)