number = int(input())

for i in range(number):
  word = input()

  if len(word) > 10:
    result = word[0] + str(len(word[1:-1])) + word[-1]
    print(result)
  else:
    print(word)