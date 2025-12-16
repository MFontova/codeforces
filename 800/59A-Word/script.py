import sys
sys.stdin = open("input.txt")

word = input()

lowers = 0
for i in range(len(word)):
    if (word[i].islower()):
        lowers += 1

if(lowers >= len(word)/2):
    print(word.lower())
else :
    print(word.upper())