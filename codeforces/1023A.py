import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    if s.find("*") != -1:
        d = deque(list(s))
        t = deque(list(t))
        while d and t:
            if d[0] == t[0]:
                d.popleft()
                t.popleft()
            else:
                break
        while d and t:
            if d[-1] == t[-1] :
                t.pop()
                d.pop()
            else:
                break
        if "".join(d) == "*" or "".join(d) == "":
            sys.stdout.write("YES")
        else:
            sys.stdout.write("NO\n")
    else:
        if s != t:
            sys.stdout.write("NO\n")
        else:
            sys.stdout.write("YES\n")


if __name__ == "__main__":
    main()