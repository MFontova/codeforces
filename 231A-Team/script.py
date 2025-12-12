number = int(input())

counter = 0
for i in range(number):
  line = input()
  n = line.count('1')
  if n > 1:
    counter += 1

print(counter)