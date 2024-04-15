import sys


temp = set(list(map(int, sys.stdin.readline().split())))
print(4 - len(temp))