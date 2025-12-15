import sys
sys.stdin = open("input.txt")

word = input()

print(word[0].upper() + word[1:])
