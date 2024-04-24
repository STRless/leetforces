import sys
from collections import Counter, defaultdict


def main():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    cnt = Counter(s)
    temp = 0
    delete = defaultdict(int)
    erased = set()
    ans = ""
    for i in range(26):
        ch = chr(ord('a')+i)
        if temp + cnt[ch] <= k:
            temp += cnt[ch]
            delete[ch] = cnt[ch]
            erased.add(ch)
        else:
            delete[ch] = k - temp
            temp = k
            erased.add(ch)
        if temp == k:
            break

    for i, ch in enumerate(s):
        if delete[ch] and ch in erased:
            delete[ch] -= 1
        elif ch not in erased or delete[ch] == 0:
            sys.stdout.write(f"{ch}")



if __name__ == "__main__":
    main()