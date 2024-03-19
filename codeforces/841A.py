import sys
from collections import Counter

def main():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()

    count = Counter(s)
    flag = True
    for key, val in count.items():
        if val > k:
            flag = False
    
    if flag:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()