import sys
sys.stdin = open("input.txt")

name = input()

chars = []

for i in name:
  if(i not in chars):
    chars.append(i)

if(len(chars) % 2 == 0):
  print('CHAT WITH HER!')
else:
  print("IGNORE HIM!" )