import sys
from collections import defaultdict

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        p = sys.stdin.readline().strip()
        s = sys.stdin.readline().strip()
        pd = {}
        for ch in p:
            if ch not in pd:
                pd[ch] = 0
            pd[ch] += 1

        flag = False
        for i in range(len(s)):
            sd = {}
            for j in range(i, len(s)):
                if s[j] not in sd:
                    sd[s[j]] = 0
                sd[s[j]] += 1
                if sd == pd:
                    flag = True
        if flag:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()