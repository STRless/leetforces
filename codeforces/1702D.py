import sys
from collections import defaultdict, Counter

def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        w = sys.stdin.readline().strip()
        p = int(sys.stdin.readline())

        cnt = Counter(w)
        total = 0
        for key, val in cnt.items():
            cost = ord(key) - ord('a') + 1
            total += (val*cost)

        deleted = defaultdict(int)
        i = 26
        while i > 0 and total > p:
            ch = chr(ord('a') + i - 1)
            while cnt[ch] > 0 and total > p:
                cnt[ch] -= 1
                deleted[ch] += 1
                total -= i
            i -= 1
        
        for ch in w:
            if deleted[ch] > 0:
                deleted[ch] -= 1
                continue
            sys.stdout.write(f"{ch}")
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()