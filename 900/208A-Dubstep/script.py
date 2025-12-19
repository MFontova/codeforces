import sys
sys.stdin = open('input.txt')

dubstep = input()

no_dubstep = [char.strip() for char in dubstep.replace('WUB', ' ').split(' ')]

words = []
for word in no_dubstep:
  if word != '':
    words.append(word)

print(' '.join(words))