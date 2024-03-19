import sys
from collections import Counter

def main():
    n = int(sys.stdin.readline())
    pups = sys.stdin.readline().strip()
    count = Counter(pups)
    flag = False
    for key, val in count.items():
        if val >= 2:
            flag = True
    if flag or len(count) == 1:
        sys.stdout.write("Yes")
    else:
        sys.stdout.write("No")


if __name__ == "__main__":
    main()