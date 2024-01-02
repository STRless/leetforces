import sys
from collections import Counter

# Topics: String, Counting, Greedy
# Time Complexity: O(n)
# Space Complexity: O(1) since count size will never exceed 52

def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        count = Counter(s)
        ans = 0
        for i in range(26):
            lower_ch = chr(ord('a') + i)
            upper_ch = chr(ord('A') + i)
            if count[lower_ch] < count[upper_ch]:
                ans += count[lower_ch]
                count[upper_ch] -= count[lower_ch]
                count[lower_ch] = 0
            else:
                ans += count[upper_ch]
                count[lower_ch] -= count[upper_ch]
                count[upper_ch] = 0
        
        for i in range(26):
            lower_ch = chr(ord('a') + i)
            upper_ch = chr(ord('A') + i)
            if count[lower_ch] > 0:
                possible = count[lower_ch] // 2
                if possible <= k:
                    k -= possible
                    ans += possible
                else:
                    ans += k
                    break
            elif count[upper_ch] > 0:
                possible = count[upper_ch] // 2
                if possible <= k:
                    k -= possible
                    ans += possible
                else:
                    ans += k
                    break


        sys.stdout.write("{}\n".format(ans))


if __name__ == "__main__":
    main()