import sys
sys.stdin = open('input.txt')

n = input()

boxes = [int(x) for x in input().split(' ')]

boxes.sort()

print( " ".join(map(str, boxes)))