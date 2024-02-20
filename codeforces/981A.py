import sys
from collections import Counter

def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    cnt = Counter(s)
    i, j = 0, n-1
    flag = False
    while i < j:
        if s[i] != s[j]:
            flag = True
            break
        i += 1
        j -= 1
    if flag:
        sys.stdout.write(f"{n}")
    elif len(cnt) == 1:
        sys.stdout.write("0")
    else:
        sys.stdout.write(f"{n-1}")


if __name__ == "__main__":
    main()