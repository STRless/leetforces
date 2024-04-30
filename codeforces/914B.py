import sys
from collections import Counter

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    cnt = Counter(arr)
    for key, val in cnt.items():
        if val % 2:
            sys.stdout.write("Conan")
            return
    sys.stdout.write("Agasa")


if __name__ == "__main__":
    main()