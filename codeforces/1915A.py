import sys
from collections import Counter

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        line = Counter(list(map(int, sys.stdin.readline().split())))
        for key, val in line.items():
            if val == 1:
                sys.stdout.write("{}\n".format(key))


if __name__ == "__main__":
    main()