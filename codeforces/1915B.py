import sys
from collections import Counter

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        grid = [set(list(sys.stdin.readline().strip())) for _ in range(3)]
        options = ['A', 'B', 'C']
        for i in range(3):
            for o in options:
                if o not in grid[i]:
                    sys.stdout.write("{}\n".format(o))


if __name__ == "__main__":
    main()