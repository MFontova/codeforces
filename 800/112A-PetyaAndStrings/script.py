import sys
sys.stdin = open("input.txt")

first = input().lower()
second = input().lower()

if(first < second):
  print(-1)

if(second < first):
  print(1)

if(first == second):
  print(0)

# if(first.lower() > second.lower()):
