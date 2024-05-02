import sys
from collections import Counter

def main():
    q = int(sys.stdin.readline())
    for _ in range(q):
        n = int(sys.stdin.readline())
        sticks = Counter(list(map(int, sys.stdin.readline().split())))



if __name__ == "__main__":
    main()