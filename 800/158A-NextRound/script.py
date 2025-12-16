import sys
sys.stdin = open("input.txt")

firstLine = input().split(' ')
secondLine = input().split(' ')

[total, cut_position] = [int(numeric_string) for numeric_string in firstLine]

participants = [int(numeric_string) for numeric_string in secondLine]

cut_value = participants[cut_position - 1]

counter = 0
for participant in participants:
  if(participant != 0):
    if(participant >= cut_value):
      counter += 1

print(counter)
  