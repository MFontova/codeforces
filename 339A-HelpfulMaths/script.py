import sys
sys.stdin = open("input.txt")

sum = input()

num_arr = sum.split('+')
num_arr.sort()
print('+'.join(num_arr))