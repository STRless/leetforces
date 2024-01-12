import sys
from collections import Counter

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()
        cnt = Counter(s)
        max_occurence = max(cnt.values())
        if max_occurence > n//2:
            sys.stdout.write(f"{max_occurence - (n - max_occurence)}\n")
        elif max_occurence == n//2:
            sys.stdout.write(f"{n - max_occurence - max_occurence}\n")
        else:
            if n % 2:
                sys.stdout.write(f"{1}\n")
            else:
                sys.stdout.write(f"{0}\n")


if __name__ == "__main__":
    main()